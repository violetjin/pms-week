#!/usr/bin/env python3
import os
import re
import sys
import argparse
from typing import List, Tuple, Dict, Any


SCORE_RE = re.compile(r"- \*\*总分：([0-9]+(?:\.[0-9]+)?) / 10\*\*")
NAME_RE = re.compile(r"- 人员：(.+?)（")
CONSISTENCY_RE = re.compile(r"- \*\*一致性评分：([^*]+)\*\*")
GITLEAKS_BLOCK_RE = re.compile(r"### 1\) gitleaks（密钥/凭证泄露）\n\n(.*?)(?:\n### 2\)|\Z)", re.S)
SEMGREP_BLOCK_RE = re.compile(r"### 2\) semgrep（安全规则）\n\n(.*?)(?:\n### 3\)|\Z)", re.S)
EST_HOURS_RE = re.compile(r"- GitLab 估算投入：([0-9]+(?:\.[0-9]+)?) 小时")
DAILY_HOURS_RE = re.compile(r"- 日报总填报工时：([0-9]+(?:\.[0-9]+)?) 小时")
RATIO_RE = re.compile(r"- 估算/填报比例：([0-9]+(?:\.[0-9]+)?)")
VAR_TASK_RE = re.compile(r"- #([^：]+)：估算 ([0-9]+(?:\.[0-9]+)?)h vs 填报 ([0-9]+(?:\.[0-9]+)?)h（误差 ([0-9]+)%）")


def read_text(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def extract_person_report(path: str) -> Dict[str, Any]:
    text = read_text(path)
    m_name = NAME_RE.search(text)
    name = m_name.group(1) if m_name else os.path.basename(path).split('_')[0]

    m_score = SCORE_RE.search(text)
    score = float(m_score.group(1)) if m_score else 0.0

    m_consistency = CONSISTENCY_RE.search(text)
    consistency = (m_consistency.group(1).strip().lower() if m_consistency else "unknown")

    est_hours = 0.0
    daily_hours = 0.0
    ratio_pct = None

    m_est = EST_HOURS_RE.search(text)
    if m_est:
        est_hours = float(m_est.group(1))

    m_daily = DAILY_HOURS_RE.search(text)
    if m_daily:
        daily_hours = float(m_daily.group(1))

    m_ratio = RATIO_RE.search(text)
    if m_ratio:
        ratio_pct = float(m_ratio.group(1))
    elif daily_hours > 0:
        ratio_pct = round(est_hours / daily_hours * 100, 1)

    gitleaks_count = 0
    semgrep_count = 0

    m_gitleaks = GITLEAKS_BLOCK_RE.search(text)
    if m_gitleaks:
        block = m_gitleaks.group(1)
        for n in re.findall(r"：([0-9]+) 条", block):
            gitleaks_count += int(n)

    m_semgrep = SEMGREP_BLOCK_RE.search(text)
    if m_semgrep:
        block = m_semgrep.group(1)
        for n in re.findall(r"：([0-9]+) 条", block):
            semgrep_count += int(n)

    variance_tasks = []
    for task_id, est, daily, diff in VAR_TASK_RE.findall(text):
        variance_tasks.append({
            "task_id": task_id,
            "estimated": float(est),
            "daily": float(daily),
            "diff_pct": int(diff),
        })

    return {
        "name": name,
        "score": score,
        "consistency": consistency,
        "gitleaks_count": gitleaks_count,
        "semgrep_count": semgrep_count,
        "risk_total": gitleaks_count + semgrep_count,
        "est_hours": est_hours,
        "daily_hours": daily_hours,
        "ratio_pct": ratio_pct,
        "variance_tasks": variance_tasks,
        "path": path,
    }


def render_score_table(rows: List[Dict[str, Any]]) -> List[str]:
    lines: List[str] = []
    lines.append('## 一、评分汇总')
    lines.append('')
    lines.append('| 排名 | 人员 | 评分 |')
    lines.append('|---|---|---:|')
    for idx, row in enumerate(sorted(rows, key=lambda x: (-x['score'], x['name'])), 1):
        lines.append(f"| {idx} | {row['name']} | {row['score']:.1f} |")
    lines.append('')
    return lines


def render_low_score_focus(rows: List[Dict[str, Any]]) -> List[str]:
    lines: List[str] = []
    lines.append('## 二、低分人员关注名单')
    lines.append('')

    focus = [r for r in rows if r['score'] < 6.0 or r['consistency'] == 'low']
    focus.sort(key=lambda x: (x['score'], x['name']))

    if not focus:
        lines.append('- 本周暂无低分或一致性偏低人员。')
        lines.append('')
        return lines

    lines.append('| 人员 | 评分 | 一致性 | 关注原因 |')
    lines.append('|---|---:|---|---|')
    for row in focus:
        reasons = []
        if row['score'] < 6.0:
            reasons.append('总分偏低')
        if row['consistency'] == 'low':
            reasons.append('提交与任务关联度偏弱')
        lines.append(f"| {row['name']} | {row['score']:.1f} | {row['consistency']} | {'；'.join(reasons)} |")
    lines.append('')
    return lines


def render_risk_summary(rows: List[Dict[str, Any]]) -> List[str]:
    lines: List[str] = []
    lines.append('## 三、风险命中汇总')
    lines.append('')

    risky = [r for r in rows if r['risk_total'] > 0]
    risky.sort(key=lambda x: (-x['risk_total'], -x['semgrep_count'], -x['gitleaks_count'], x['name']))

    if not risky:
        lines.append('- 本周未发现风险命中记录。')
        lines.append('')
        return lines

    lines.append('| 人员 | 风险总数 | gitleaks | semgrep |')
    lines.append('|---|---:|---:|---:|')
    for row in risky:
        lines.append(f"| {row['name']} | {row['risk_total']} | {row['gitleaks_count']} | {row['semgrep_count']} |")
    lines.append('')
    return lines


def render_effort_variance(rows: List[Dict[str, Any]]) -> List[str]:
    lines: List[str] = []
    lines.append('## 四、工时偏差较大人员汇总')
    lines.append('')

    variance_rows = []
    for row in rows:
        ratio = row['ratio_pct']
        if ratio is None:
            continue
        if ratio < 80 or ratio > 120:
            variance_rows.append(row)

    variance_rows.sort(key=lambda x: (abs((x['ratio_pct'] or 100) - 100), x['name']), reverse=True)

    if not variance_rows:
        lines.append('- 本周暂无工时偏差较大人员。')
        lines.append('')
        return lines

    lines.append('| 人员 | GitLab估算工时 | 日报填报工时 | 估算/填报比例 | 说明 |')
    lines.append('|---|---:|---:|---:|---|')
    for row in variance_rows:
        ratio = row['ratio_pct'] or 0.0
        if ratio < 80:
            note = '填报工时明显高于代码侧估算'
        else:
            note = '代码侧估算明显高于填报工时'
        lines.append(f"| {row['name']} | {row['est_hours']:.2f} | {row['daily_hours']:.2f} | {ratio:.0f}% | {note} |")
    lines.append('')

    detail_rows = [r for r in variance_rows if r['variance_tasks']]
    if detail_rows:
        lines.append('### 工时偏差任务明细')
        lines.append('')
        for row in detail_rows:
            lines.append(f"- **{row['name']}**")
            for t in row['variance_tasks'][:5]:
                lines.append(f"  - #{t['task_id']}：估算 {t['estimated']:.2f}h vs 填报 {t['daily']:.2f}h（误差 {t['diff_pct']}%）")
        lines.append('')

    return lines


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', required=True, help='weekly report directory, e.g. logs/20260309')
    args = ap.parse_args()

    report_dir = args.dir
    rows: List[Dict[str, Any]] = []
    for fn in os.listdir(report_dir):
        if not fn.endswith('_week.md'):
            continue
        if '周汇总' in fn:
            continue
        path = os.path.join(report_dir, fn)
        try:
            rows.append(extract_person_report(path))
        except Exception:
            continue

    folder = os.path.basename(report_dir)
    out_path = os.path.join(report_dir, f'{folder}_周汇总.md')

    lines: List[str] = []
    lines.append('# 开发人员周汇总')
    lines.append('')
    lines.extend(render_score_table(rows))
    lines.extend(render_low_score_focus(rows))
    lines.extend(render_risk_summary(rows))
    lines.extend(render_effort_variance(rows))

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(out_path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
