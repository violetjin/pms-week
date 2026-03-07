#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""AIBase AI日报抓取 + 汇总发送（企业微信机器人）

目标：
- 抓取 https://news.aibase.com/zh/daily 列表页
- 解析最新一期 /zh/daily/<id>
- 抓取详情页，提取新闻条目（尽量找到 /zh/news/<id>）
- 逐条抓取新闻页，提取正文并补全原文外链（若能找到）
- 交给 LLM 生成中文高密度汇总（Markdown）
- 按 <=3500 汉字拆分，调用 skills/wecom-webhook/scripts/send_wecom_webhook.py 发送

说明：
- 这个脚本尽量“程序化抽取 + 结构化喂给 LLM”，避免页面噪声导致英文/乱码主导。
- 失败时会输出：错误原因 + 已尝试步骤，并以“本次未能生成汇总”结束（不发送）。
"""

from __future__ import annotations

import argparse
import datetime as _dt
import html
import json
import os
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass, asdict
from typing import Iterable, Optional, Tuple, List, Dict
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE = "https://news.aibase.com"
DAILY_LIST_URL = f"{BASE}/zh/daily"

WORKSPACE = Path("/home/jinye/.openclaw/workspace")
DAILY_DIR = WORKSPACE / "daily"
LOG_DIR = DAILY_DIR / "log"


@dataclass
class NewsItem:
    title: str
    news_url: Optional[str] = None          # https://news.aibase.com/zh/news/<id>
    external_url: Optional[str] = None      # 新闻页里指向站外原文的链接（如果能找到）
    summary: Optional[str] = None           # 摘要：优先使用【AiBase提要:】抽取
    entities: Optional[List[str]] = None    # 粗略实体（公司/模型/产品）
    body_text: Optional[str] = None         # 新闻页正文（清洗后，截断）


COMMON_ENTITIES = [
    "OpenAI", "Google", "DeepMind", "Meta", "Anthropic", "NVIDIA", "Microsoft", "Apple",
    "阿里", "腾讯", "字节", "华为", "百度", "京东", "小米",
    "DeepSeek", "Qwen", "通义", "Gemini", "Claude", "Llama", "Mistral", "Stable Diffusion",
    "MiniMax", "Kimi", "智谱", "GLM", "OpenRouter", "Suno"
]


def _fix_text(raw: str) -> str:
    if raw is None:
        return ""
    # 仅做 HTML 实体修复；不要做 latin1->utf8“修复”（会破坏正常中文）
    raw = html.unescape(raw)
    raw = re.sub(r"\s+", " ", str(raw)).strip()
    return raw


def _session() -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.6",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive",
    })
    return s


def fetch_html(s: requests.Session, url: str, timeout: int = 20) -> str:
    r = s.get(url, timeout=timeout)
    r.raise_for_status()
    # 站点实际为 utf-8，但 requests 有时会误判（例如 Windows-1254），导致中文乱码
    try:
        r.encoding = "utf-8"
    except Exception:
        pass
    return r.text


def parse_latest_daily_url(list_html: str) -> Tuple[str, str]:
    soup = BeautifulSoup(list_html, "lxml")
    hrefs = [a.get("href") for a in soup.select("a[href]")]
    ids = []
    for href in hrefs:
        if not href:
            continue
        m = re.search(r"^/zh/daily/(\d+)$", href)
        if m:
            ids.append(int(m.group(1)))
    if not ids:
        raise ValueError("列表页未解析到最新一期详情路径（未发现 /zh/daily/<id> 链接）")
    latest_id = str(max(ids))
    return latest_id, f"{BASE}/zh/daily/{latest_id}"


def extract_items_from_daily(daily_html: str) -> Tuple[str, List[NewsItem]]:
    """从日报详情页抽取：日报标题 + 条目列表（按编号 1、2、3… 或 一、二、三… 分段）。

    规则：
    - h1 或第一行文字作为主题
    - 按编号条目（1、2、3… 或 一、二、三…）切分正文，每条提取标题 + 要点
    - 要点优先取该条内的【AiBase提要:】；否则用该条正文做约 50 字摘要
    """
    soup = BeautifulSoup(daily_html, "lxml")

    # 主题：优先 h1，其次正文第一行
    h1 = soup.select_one("h1")
    if h1:
        daily_title = _fix_text(h1.get_text(" ", strip=True))
    else:
        # 回退：取正文第一个非空文本作为主题
        body = soup.select_one("main") or soup
        for el in body.descendants:
            if getattr(el, "name", None) in ["script", "style", "meta"]:
                continue
            txt = _fix_text(el.get_text(" ", strip=True))
            if txt and len(txt) >= 10:
                daily_title = txt
                break
        else:
            daily_title = ""

    # 抓取正文（跳过 header/footer/导航等明显噪音）
    main = soup.select_one("article") or soup.select_one("main") or soup
    for skip in main.select("header, footer, nav, script, style, .recommend, .related, .sidebar"):
        skip.decompose()

    # 整体文本，按编号切分条目
    # 注意：这里需要保留换行以识别“行首编号”。不要用 _fix_text（会把换行压成空格）。
    whole_text = html.unescape(main.get_text("\n", strip=True))
    whole_text = re.sub(r"\r\n?", "\n", whole_text)
    # 匹配编号：
    # - 行首的 1、 2、...
    # - 行首的 一、二、...
    # - 行首的 (1)（1） 或 1.
    split_pat = r"(?:^|\n)\s*(?:\d+、|[一二三四五六七八九十]+、|\(\d+\)|（\d+）|\d+\.)\s*"
    parts = re.split(split_pat, whole_text)

    # 去掉第一部分（通常是导航/欢迎语/导语）
    if len(parts) > 1:
        parts = parts[1:]

    # 进一步过滤掉明显的导航残留
    junk_prefix = ("AI资讯", "最新AI日报", "正文", "首页", "AI产品库", "模型广场")
    parts = [p for p in parts if p.strip() and not p.strip().startswith(junk_prefix)]

    items: List[NewsItem] = []
    for p in parts:
        p = p.strip()
        if not p or len(p) < 10:
            continue
        # 取第一行作为标题
        first_line = p.split("\n")[0].strip()
        # 过滤明显不是标题的行
        if re.match(r"^[\d一二三四五六七八九十\(（][\d一二三四五六七八九十).、）]*\s*$", first_line):
            # 可能是重复编号，跳过
            continue

        # 从整段提取【AiBase提要:】
        aibase_summary = None
        m = re.search(r"【\s*AiBase提要\s*:?\s*】\s*(.+?)\s*(?:【|$)", p, flags=re.I | re.S)
        if m:
            aibase_summary = m.group(1).strip()

        item = NewsItem(title=first_line)
        if aibase_summary:
            # 尽量保留 emoji bullet 格式
            item.summary = truncate(aibase_summary, 800, add_ellipsis=False)
        else:
            # 用整段做摘要（取前 50 字）
            item.summary = _summarize_50_zh(p)

        items.append(item)

    if not items:
        raise ValueError("详情页未解析到编号条目（未发现 1、2、3… 或 一、二、三… 格式的条目）")

    return daily_title, items


def extract_article(soup: BeautifulSoup) -> Tuple[str, str, Optional[str]]:
    # 站点结构不确定：优先 article，其次 main
    node = soup.select_one("article") or soup.select_one("main") or soup
    title = _fix_text((soup.select_one("h1") or node.select_one("h1") or node.select_one("h2") or soup).get_text(" ", strip=True))

    # 正文：取 node 下的 p/li 文本
    parts = []
    for el in node.select("p, li"):
        txt = _fix_text(el.get_text(" ", strip=True))
        if txt and len(txt) >= 10:
            parts.append(txt)
    body = "\n".join(parts)

    # 若包含【AiBase提要:】则优先提取该段作为摘要
    aibase_summary = None
    m = re.search(r"【\s*AiBase提要\s*:?\s*】\s*(.+)$", body, flags=re.I)
    if m:
        aibase_summary = m.group(1).strip()
        # 常见是多条 emoji/要点拼在一起，这里尽量压缩空白
        aibase_summary = re.sub(r"\s+", " ", aibase_summary)

    # 去掉明显的噪声：过多数字/浏览量等
    body = re.sub(r"\b\d{1,4}\.\d+k\b", "", body, flags=re.I)
    body = re.sub(r"\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b", "", body)
    body = re.sub(r"\s+", " ", body).strip()

    return title, body, aibase_summary


def guess_entities(text: str) -> List[str]:
    found = []
    for e in COMMON_ENTITIES:
        if e.lower() in text.lower():
            found.append(e)
    # 去重保持顺序
    out = []
    seen = set()
    for x in found:
        if x not in seen:
            out.append(x)
            seen.add(x)
    return out


def find_external_url(news_soup: BeautifulSoup) -> Optional[str]:
    # 常见：正文里会有站外链接；过滤 aibase 自己域名
    links = []
    for a in news_soup.select("a[href]"):
        href = a.get("href")
        if not href:
            continue
        href = href.strip()
        if href.startswith("/"):
            href = BASE + href
        if not re.match(r"^https?://", href):
            continue
        if href.startswith(BASE):
            continue
        # 排除一些无意义链接
        if any(x in href.lower() for x in ["javascript:", "mailto:"]):
            continue
        links.append(href)
    return links[0] if links else None


def truncate(text: str, max_chars: int, add_ellipsis: bool = True) -> str:
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars].rstrip()
    return (cut + "…") if add_ellipsis else cut


def split_markdown(content: str, max_chars: int = 3800) -> List[str]:
    """按段落拆分，确保每段 <=3800 字符（企业微信 markdown 限制 4096，留 296 字缓冲）。

    优先保持段落完整；若某段超长，则硬切（尽量在换行处，不截断 URL）。
    如果整段内容 <=3800，直接返回单 chunk；超过才拆。
    """
    if len(content) <= max_chars:
        return [content]

    # 先按段落切
    paras = [p for p in content.split("\n\n") if p.strip()]
    chunks = []
    cur = ""

    for p in paras:
        # 单段直接超长：硬切
        if len(p) > max_chars:
            start = 0
            while start < len(p):
                cut = min(start + max_chars, len(p))
                piece = p[start:cut]
                # 尽量避免截断 URL
                if "http" in piece[-80:]:
                    # 找到最近的换行
                    last_br = piece.rfind("\n")
                    if last_br > 0:
                        piece = piece[:last_br].rstrip()
                        cut = start + last_br
                chunks.append(piece.strip())
                start = cut
        else:
            # 段落可容纳
            if not cur:
                cur = p
                continue
            if len(cur) + 2 + len(p) <= max_chars:
                cur += "\n\n" + p
            else:
                chunks.append(cur)
                cur = p
    if cur:
        chunks.append(cur)
    return chunks


def _clean_noise(text: str) -> str:
    if not text:
        return ""
    text = _fix_text(text)
    # 去掉常见“阅读量/时间戳/孤立数字串”等噪声
    text = re.sub(r"\b\d{1,4}\.\d+k\b", "", text, flags=re.I)
    text = re.sub(r"\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _summarize_50_zh(text: str, max_chars: int = 50) -> str:
    """不用 LLM 的简易 50 字摘要：取前若干句并清洗压缩。"""
    text = _clean_noise(text)
    if not text:
        return ""
    # 优先按中文句号/分号/换行切句
    parts = re.split(r"[。；;\n]+", text)
    parts = [p.strip() for p in parts if p.strip()]
    s = "，".join(parts[:2]) if parts else text
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > max_chars:
        s = s[:max_chars].rstrip() + "…"
    return s


def render_markdown(structured: dict) -> str:
    """纯脚本生成 markdown（日更稳定，不依赖 LLM）。"""
    daily_url = structured.get("daily_url")
    daily_title = structured.get("daily_title")
    items = structured.get("items", [])

    lines = ["AIBase AI日报汇总"]
    if daily_title:
        lines.append(f"一、{daily_title}")
    lines.append(f"来源：{daily_url}")
    lines.append("")

    for it in items:
        title = _fix_text(it.get("title") or "")
        link = it.get("external_url") or it.get("news_url") or daily_url
        summary = it.get("summary")
        if summary:
            summary = _clean_noise(summary)
        else:
            summary = _summarize_50_zh(it.get("body_text") or "")
        if not summary:
            summary = "（未提取到摘要）"

        lines.append(f"- **{title}**")
        lines.append(f"  - 摘要：{summary}")
        lines.append("")

    return "\n".join(lines).strip()


def send_wecom(webhook_url: str, markdown_text: str) -> List[Tuple[int, str]]:
    script = "/home/jinye/.openclaw/workspace/skills/wecom-webhook/scripts/send_wecom_webhook.py"
    chunks = split_markdown(markdown_text, max_chars=3800)
    results = []
    total = len(chunks)
    for i, ch in enumerate(chunks, start=1):
        prefix = f"（{i}/{total}）\n" if total > 1 else ""
        content = prefix + ch
        p = subprocess.run(
            ["python3", script, "--url", webhook_url, "--msgtype", "markdown", "--text", content],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        out = (p.stdout or "").strip()
        err = (p.stderr or "").strip()
        msg = out or err or "(no output)"
        # 兼容脚本输出 JSON 或纯文本
        results.append((p.returncode, msg))
    return results


def _write_log(log_path: Path, text: str):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(text, encoding="utf-8")


def _purge_old_logs(log_dir: Path, keep_days: int = 7):
    if not log_dir.exists():
        return
    cutoff = _dt.datetime.now() - _dt.timedelta(days=keep_days)
    for p in log_dir.glob("*.log"):
        try:
            ts = _dt.datetime.fromtimestamp(p.stat().st_mtime)
            if ts < cutoff:
                p.unlink(missing_ok=True)
        except Exception:
            # 不因为清理失败影响主流程
            pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--webhook", required=True, help="企业微信机器人 webhook url")
    ap.add_argument("--max-items", type=int, default=30, help="最多处理新闻条数")
    ap.add_argument("--dry-run", action="store_true", help="不发送，仅打印执行汇报")
    ap.add_argument("--log-dir", default=str(LOG_DIR), help="日志目录（默认 workspace/daily/log）")
    ap.add_argument("--keep-log-days", type=int, default=7, help="保留日志天数（默认 7）")
    args = ap.parse_args()

    log_dir = Path(args.log_dir)
    _purge_old_logs(log_dir, keep_days=args.keep_log_days)
    log_path = log_dir / ( _dt.date.today().isoformat() + ".log" )

    tried = []
    report_lines = []

    try:
        s = _session()

        tried.append(f"抓取列表页 {DAILY_LIST_URL}")
        list_html = fetch_html(s, DAILY_LIST_URL)
        daily_id, daily_url = parse_latest_daily_url(list_html)

        tried.append(f"抓取最新一期详情页 {daily_url}")
        daily_html = fetch_html(s, daily_url)
        daily_title, items = extract_items_from_daily(daily_html)
        items = items[: args.max_items]

        # 抓取每条新闻页补全
        for it in items:
            if not it.news_url:
                continue
            tried.append(f"抓取新闻页 {it.news_url}")
            nh = fetch_html(s, it.news_url)
            soup = BeautifulSoup(nh, "lxml")
            title, body, aibase_summary = extract_article(soup)
            if title and (not it.title or it.title.startswith("AIBase 新闻")):
                it.title = title
            it.body_text = truncate(body, 1200)
            it.summary = truncate(aibase_summary, 800, add_ellipsis=False) if aibase_summary else None
            it.external_url = find_external_url(soup)
            it.entities = guess_entities((it.title or "") + "\n" + (it.summary or "") + "\n" + (it.body_text or ""))

        # 去重（按 title 或 URL）
        dedup = []
        seen_title = set()
        seen_url = set()
        for it in items:
            tkey = (it.title or "").strip().lower()
            ukey = (it.external_url or it.news_url or "").strip().lower()
            if tkey and tkey in seen_title:
                continue
            if ukey and ukey in seen_url:
                continue
            if tkey:
                seen_title.add(tkey)
            if ukey:
                seen_url.add(ukey)
            dedup.append(it)

        structured = {
            "source": "AIBase AI日报",
            "daily_id": daily_id,
            "daily_url": daily_url,
            "daily_title": daily_title,
            "generated_at": _dt.datetime.now().isoformat(timespec="seconds"),
            "items": [asdict(x) for x in dedup],
        }

        md = render_markdown(structured)

        send_results = []
        if not args.dry_run:
            # 兜底：有时外部传入的 webhook 会被误拼（例如重复域名 qyapi.weixin.qqapi.weixin.qq.com）
            # 这里做一次“明显错误”的自动修复，避免 DNS 解析失败导致整天不送达。
            fixed_webhook = args.webhook.replace("qyapi.weixin.qqapi.weixin.qq.com", "qyapi.weixin.qq.com")
            send_results = send_wecom(fixed_webhook, md)

        # 最终执行汇报（不回显正文）
        report_lines.append(f"日报期号/URL：{daily_id} {daily_url}")
        if args.dry_run:
            report_lines.append("发送分片数量：0（dry-run）")
        else:
            report_lines.append(f"发送分片数量：{len(send_results)}")
            for i, (rc, msg) in enumerate(send_results, start=1):
                m = re.search(r"\"errcode\"\s*:\s*(\d+).*?\"errmsg\"\s*:\s*\"([^\"]+)\"", msg)
                if m:
                    report_lines.append(f"分片{i}/{len(send_results)}：errcode={m.group(1)} errmsg={m.group(2)} (returncode={rc})")
                else:
                    report_lines.append(f"分片{i}/{len(send_results)}：{msg} (returncode={rc})")

        final_report = "\n".join(report_lines)
        print(final_report)
        _write_log(log_path, final_report + "\n")

    except Exception as e:
        err_lines = [f"错误原因: {e}", "", "已尝试步骤:"]
        for step in tried[:30]:
            err_lines.append(f"- {step}")
        err_lines.append("\n本次未能生成汇总")
        final_report = "\n".join(err_lines)
        print(final_report)
        _write_log(log_path, final_report + "\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
