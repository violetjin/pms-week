#!/usr/bin/env python3
"""Analyze weekly GitLab commits vs ZenTao tasks to generate per-developer reports.

Inputs:
  - gitlab_weekly_JSON: from fetch_gitlab_weekly.py
  - zentao_weekly_JSON: from fetch_zentao_weekly.py

Outputs:
  - logs/姓名_YYYY-MM-DD_YYYY-MM-DD_week.md (per developer)
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from typing import Dict, Any, List
import subprocess


def load_users(users_file: str) -> Dict[str, str]:
    """Load users.txt: account|name mapping."""
    m: Dict[str, str] = {}
    try:
        f = open(users_file, "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
    except UnicodeDecodeError:
        f = open(users_file, "r", encoding="gb18030")
        lines = f.readlines()
        f.close()

    for line in lines:
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if "|" in s:
            a, n = s.split("|", 1)
            a = a.strip()
            n = n.strip()
            if a:
                m[a] = n
        else:
            m[s] = ""
    return m


def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def estimate_hours_by_session(commits: List[Dict[str, Any]], gap_minutes: int = 90, pad_minutes: int = 20) -> float:
    """Estimate hours by session heuristic."""
    if not commits:
        return 0.0
    from datetime import datetime as dt, timedelta
    def parse_iso(s: str) -> dt:
        return dt.fromisoformat(s.replace("Z", "+00:00"))

    sorted_commits = sorted(commits, key=lambda c: parse_iso(c.get("authored_date", "")))
    gap = timedelta(minutes=gap_minutes)
    pad = timedelta(minutes=pad_minutes)

    total = timedelta(0)
    session_start = parse_iso(sorted_commits[0].get("authored_date", ""))
    last = session_start

    for c in sorted_commits[1:]:
        t = parse_iso(c.get("authored_date", ""))
        if t - last > gap:
            total += (last - session_start) + pad
            session_start = t
        last = t

    total += (last - session_start) + pad
    return max(0.0, total.total_seconds() / 3600.0)


def estimate_hours_by_churn(commits: List[Dict[str, Any]], loc_per_hour: int = 200, min_h: float = 0.25, max_h: float = 10.0) -> float:
    """Estimate hours by churn (LOC changed) heuristic."""
    total_h = 0.0
    for c in commits:
        churn = (c.get("additions") or 0) + (c.get("deletions") or 0)
        if churn <= 0:
            continue
        h = churn / float(loc_per_hour)
        h = max(min_h, min(max_h, h))
        total_h += h
    return total_h


def is_merge_commit(commit_title: str) -> bool:
    """Return True when the commit title is a merge commit."""
    title = (commit_title or "").strip().lower()
    return title.startswith("merge ")


TASK_ID_PATTERNS = [
    re.compile(r"#(\d{4,})\b"),
    re.compile(r"\b(\d{4,})\s*[-:：]"),
    re.compile(r"^revert\s+[\"'].*?#?(\d{4,})\b", re.IGNORECASE),
]


def extract_task_ids(commit_title: str) -> List[str]:
    """Extract task ids from commit titles.

    Supports patterns such as:
    - #44372 xxx
    - 44372 - xxx
    - Revert "44372 - xxx"
    """
    title = (commit_title or "").strip()
    if not title or is_merge_commit(title):
        return []

    found: List[str] = []
    for pattern in TASK_ID_PATTERNS:
        for match in pattern.findall(title):
            task_id = match if isinstance(match, str) else match[0]
            if task_id and task_id not in found:
                found.append(task_id)
    return found


def extract_commit_subject(commit_title: str) -> str:
    """Extract module/intent from commit title."""
    m = re.match(r"^(feat|fix|docs|style|refactor|perf|test|chore)(\(.+\))?:\s*(.*)$", commit_title, re.IGNORECASE)
    if m:
        return f"{m.group(1)}: {m.group(3)}"
    if extract_task_ids(commit_title):
        return commit_title
    return commit_title[:30]


def build_commit_summary(commits: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Group commits by project and summarize."""
    by_project: Dict[str, List[Dict[str, Any]]] = {}
    for c in commits:
        proj = c.get("project_name", "unknown")
        if proj not in by_project:
            by_project[proj] = []
        by_project[proj].append(c)

    summaries = []
    for proj, projs in by_project.items():
        subjects = [extract_commit_subject(c.get("title", "")) for c in projs]
        summaries.append({
            "project": proj,
            "commits_count": len(projs),
            "subjects": subjects[:5],
            "total_loc": sum((c.get("additions") or 0) + (c.get("deletions") or 0) for c in projs),
        })
    return summaries


def build_task_summary(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Summarize tasks by category and system."""
    by_class: Dict[str, int] = {}
    by_system: Dict[str, int] = {}
    for t in tasks:
        cls = t.get("任务分类", "未知")
        sys_name = t.get("系统名称", "未知")
        by_class[cls] = by_class.get(cls, 0) + 1
        by_system[sys_name] = by_system.get(sys_name, 0) + 1

    return {
        "total": len(tasks),
        "by_classification": by_class,
        "by_system": by_system,
    }


def calculate_consistency(commits: List[Dict[str, Any]], tasks: List[Dict[str, Any]]) -> tuple[str, str]:
    """Estimate consistency between commits and tasks."""
    commits_with_taskid = 0
    for c in commits:
        title = c.get("title", "")
        if extract_task_ids(title):
            commits_with_taskid += 1

    if not commits:
        return "low", "无代码提交"

    ratio = commits_with_taskid / len(commits)
    if ratio >= 0.8:
        return "high", f"{ratio*100:.0f}% 提交包含任务ID"
    elif ratio >= 0.5:
        return "medium", f"{ratio*100:.0f}% 提交包含任务ID"
    else:
        return "low", f"{ratio*100:.0f}% 提交包含任务ID，建议在提交信息中关联任务ID"


def run_security_scan(tmp_dir: str, report_name: str) -> tuple[List[Dict], List[Dict]]:
    """Run gitleaks and semgrep security scans."""
    import json as json_lib
    
    gitleaks_report = os.path.join(tmp_dir, f"gitleaks_{report_name}.json")
    semgrep_report = os.path.join(tmp_dir, f"semgrep_{report_name}.json")
    
    gitleaks_result = []
    try:
        result = subprocess.run(
            ["gitleaks", "detect", "--source", "/home/jinye/.openclaw/workspace", "--report-format", "json", "--report-path", gitleaks_report],
            capture_output=True,
            text=True,
            timeout=180
        )
        if result.returncode == 0 or result.returncode == 1:
            with open(gitleaks_report, "r") as f:
                gitleaks_data = json_lib.load(f)
            gitleaks_result = gitleaks_data if isinstance(gitleaks_data, list) else gitleaks_data.get("findings", [])
    except Exception as e:
        gitleaks_result = []
    
    semgrep_result = []
    try:
        result = subprocess.run(
            ["semgrep", "--json", "--output", semgrep_report, "/home/jinye/.openclaw/workspace"],
            capture_output=True,
            text=True,
            timeout=180
        )
        if result.returncode == 0:
            with open(semgrep_report, "r") as f:
                semgrep_data = json_lib.load(f)
            semgrep_result = semgrep_data.get("results", [])
    except Exception as e:
        semgrep_result = []
    
    return gitleaks_result, semgrep_result


def group_by_repo_gitleaks(gitleaks_result: List[Dict]) -> Dict[str, List[Dict]]:
    """Group gitleaks findings by repository."""
    by_repo: Dict[str, List[Dict]] = {}
    for finding in gitleaks_result:
        file_path = finding.get("File", finding.get("file", ""))
        if not file_path.startswith("/home/jinye/.openclaw/workspace"):
            file_path = os.path.join("/home/jinye/.openclaw/workspace", file_path)
        
        project_short = "unknown"
        for part in file_path.split("/"):
            if part.startswith("bdo-"):
                project_short = part
                break
        
        if project_short not in by_repo:
            by_repo[project_short] = []
        by_repo[project_short].append(finding)
    return by_repo


def group_by_repo_semgrep(semgrep_result: List[Dict]) -> Dict[str, List[Dict]]:
    """Group semgrep findings by repository."""
    by_repo: Dict[str, List[Dict]] = {}
    for match in semgrep_result:
        file_path = match.get("path", "")
        
        project_short = "unknown"
        for part in file_path.split("/"):
            if part.startswith("bdo-"):
                project_short = part
                break
        
        if project_short not in by_repo:
            by_repo[project_short] = []
        by_repo[project_short].append(match)
    return by_repo


def generate_markdown_report(
    username: str,
    realname: str,
    gitlab_data: Dict[str, Any],
    zentao_data: Dict[str, Any],
    output_path: str,
):
    """Generate markdown report for one developer."""
    from datetime import datetime as dt

    # Extract data
    user_git = gitlab_data.get("users", {}).get(username, {})
    user_zt = zentao_data.get("users", {}).get(username, {})

    commits = user_git.get("commits", [])
    tasks = user_zt.get("tasks", [])

    git_counts = user_git.get("counts", {})
    zt_summary = build_task_summary(tasks)
    consistency, consistency_note = calculate_consistency(commits, tasks)

    git_summary = build_commit_summary(commits)
    session_h = estimate_hours_by_session(commits)
    churn_h = estimate_hours_by_churn(commits)
    combined_h = max(session_h, churn_h)

    # Date range
    range_from = gitlab_data.get("date_range", {}).get("from_iso", "")
    range_until = gitlab_data.get("date_range", {}).get("until_iso", "")

    try:
        from_dt = dt.fromisoformat(range_from)
        until_dt = dt.fromisoformat(range_until)
        from_shanghai = from_dt.astimezone(timezone(timedelta(hours=8)))
        until_shanghai = until_dt.astimezone(timezone(timedelta(hours=8)))
        from_date = from_shanghai.strftime("%Y-%m-%d")
        until_date = (until_shanghai - timedelta(days=1)).strftime("%Y-%m-%d")
    except Exception:
        from_date = range_from[:10]
        until_date = range_until[:10]

    # Build markdown
    lines = []
    lines.append(f"# 开发人员周报（GitLab + 禅道）")
    lines.append("")
    lines.append(f"- 人员：{realname}（{username}）")
    lines.append(f"- 时间范围：{from_date} ~ {until_date}（上周一 00:00 - 周日 24:00）")
    lines.append(f"- 覆盖范围：所有项目")
    lines.append("")
    lines.append("## 一、GitLab 提交概览")
    lines.append("")
    lines.append(f"- 提交次数：{git_counts.get('commits', 0)} commits")
    lines.append(f"- 代码变更量：{git_counts.get('loc_total', 0)} LOC")
    lines.append(f"- 估算投入：{combined_h:.2f} 小时（combined: session+churn）")
    lines.append(f"- 效率指标：LOC/h ≈ {round(git_counts.get('loc_total', 0) / max(combined_h, 0.01), 0)}, commits/h ≈ {round(git_counts.get('commits', 0) / max(combined_h, 0.01), 2)}")
    lines.append("")
    lines.append("### 按项目汇总")
    for s in git_summary:
        lines.append(f"- **{s['project']}**：{s['commits_count']} commits, {s['total_loc']} LOC")
        for sub in s['subjects'][:3]:
            lines.append(f"  - {sub}")
    lines.append("")
    lines.append("## 二、禅道任务概览")
    lines.append("")
    lines.append(f"- 任务数：{zt_summary['total']}")
    lines.append("")
    lines.append("### 分类分布")
    for cls, cnt in zt_summary['by_classification'].items():
        lines.append(f"- {cls}：{cnt}")
    lines.append("")
    lines.append("### 系统分布")
    for sys, cnt in zt_summary['by_system'].items():
        lines.append(f"- {sys}：{cnt}")
    lines.append("")
    lines.append("### 任务列表")
    if tasks:
        for t in tasks:
            ticket_id = t.get('任务ID', '')
            title = t.get('任务标题', '')
            system = t.get('系统名称', '')
            if ticket_id:
                lines.append(f"- #{ticket_id} {title}（{system}）")
            else:
                lines.append(f"- {title}（{system}）")
    else:
        lines.append("（无任务记录）")
    lines.append("")
    
    # 日报汇总
    daily_reports = user_zt.get("daily_reports", [])
    daily_total_hours = 0.0
    daily_by_ticket: Dict[str, float] = {}
    daily_by_date: Dict[str, float] = {}
    ticket_titles: Dict[str, str] = {}
    if daily_reports:
        for d in daily_reports:
            hours = float(d.get("任务花费时间") or 0)
            daily_total_hours += hours
            ticket_id = d.get("任务ID")
            ticket_title = d.get("任务标题", "")
            if ticket_id:
                daily_by_ticket[str(ticket_id)] = daily_by_ticket.get(str(ticket_id), 0.0) + hours
                if str(ticket_id) not in ticket_titles and ticket_title:
                    ticket_titles[str(ticket_id)] = ticket_title
            report_date = d.get("填报日期", "")
            if report_date:
                daily_by_date[report_date] = daily_by_date.get(report_date, 0.0) + hours
    
    lines.append("### 日报汇总")
    lines.append(f"- 日报填报总工时：{daily_total_hours:.2f} 小时")
    if daily_by_date:
        lines.append("- 每日填报工时：")
        for date in sorted(daily_by_date.keys()):
            lines.append(f"  - {date}：{daily_by_date[date]:.2f} 小时")
    else:
        lines.append("- （无日报记录）")
    if daily_by_ticket:
        lines.append("- 按任务统计：")
        sorted_tickets = sorted(daily_by_ticket.items(), key=lambda x: x[1], reverse=True)[:5]
        for tid, hrs in sorted_tickets:
            title = ticket_titles.get(tid, "")
            lines.append(f"  - #{tid} {title}：{hrs:.2f} 小时")
    lines.append("")

    lines.append("## 三、一致性分析")
    lines.append("")

    commits_with_taskid = 0
    commits_without_taskid = []
    commits_merge = []
    for c in commits:
        title = c.get("title", "")
        task_ids = extract_task_ids(title)
        if task_ids:
            commits_with_taskid += 1
        elif is_merge_commit(title):
            commits_merge.append(title)
        else:
            commits_without_taskid.append(title)

    if not commits:
        consistency = "low"
        consistency_note = "无代码提交"
    else:
        ratio = commits_with_taskid / len(commits)
        if ratio >= 0.8:
            consistency = "high"
            consistency_note = f"{ratio*100:.0f}% 提交包含任务ID"
        elif ratio >= 0.5:
            consistency = "medium"
            consistency_note = f"{ratio*100:.0f}% 提交包含任务ID"
        else:
            consistency = "low"
            consistency_note = f"{ratio*100:.0f}% 提交包含任务ID，建议在提交信息中关联任务ID"

    lines.append(f"- **一致性评分：{consistency}**")
    lines.append(f"- 说明：{consistency_note}")
    lines.append("")

    lines.append("#### 提交内容检查")
    lines.append(f"- 包含任务ID的提交：{commits_with_taskid}/{len(commits)}")
    if commits_merge:
        lines.append(f"- Merge 提交：{len(commits_merge)}")
        for m in commits_merge[:3]:
            lines.append(f"  - {m}")
    if commits_without_taskid:
        lines.append(f"- **未包含任务ID且非 Merge 的提交（需重点关注）：{len(commits_without_taskid)}**")
        for m in commits_without_taskid[:3]:
            lines.append(f"  - {m}")
    lines.append("")

    lines.append("#### 工时对比分析")
    lines.append(f"- GitLab 估算投入：{combined_h:.2f} 小时")
    lines.append(f"- 日报总填报工时：{daily_total_hours:.2f} 小时")
    if daily_total_hours > 0:
        ratio_hours = combined_h / daily_total_hours
        lines.append(f"- 估算/填报比例：{ratio_hours:.2f}x")
        lines.append("")

        lines.append("#### 工时误差 > 100% 的任务（填报工时 > 2x 估算）")
        high_variance_tasks = []
        for ticket_id, daily_h in daily_by_ticket.items():
            ticket_commits = [c for c in commits if str(ticket_id) in extract_task_ids(c.get("title", ""))]
            if ticket_commits:
                ticket_session_h = estimate_hours_by_session(ticket_commits)
                ticket_churn_h = estimate_hours_by_churn(ticket_commits)
                ticket_estimated = max(ticket_session_h, ticket_churn_h)
                if daily_h > ticket_estimated * 2 and ticket_estimated > 0.1:
                    high_variance_tasks.append((ticket_id, ticket_estimated, daily_h))
            else:
                if daily_h > 1.0:
                    high_variance_tasks.append((ticket_id, 0.5, daily_h))

        if high_variance_tasks:
            for tid, est, daily in high_variance_tasks[:5]:
                lines.append(f"- #{tid}：估算 {est:.2f}h vs 填报 {daily:.2f}h（误差 {((daily-est)/est*100):.0f}%）")
        else:
            lines.append("（无明显工时误差记录）")
    else:
        lines.append("- 无日报记录，无法进行工时对比")
    lines.append("")
    lines.append("")

    # 4. 安全扫描（gitleaks + semgrep）
    lines.append("## 四、风险提示")
    lines.append("")
    
    if commits:
        # 创建临时目录（在日期文件夹下）
        tmp_dir = os.path.join(os.path.dirname(output_path), "tmp")
        os.makedirs(tmp_dir, exist_ok=True)
        
        # 运行安全扫描
        report_name = os.path.basename(output_path)
        gitleaks_result, semgrep_result = run_security_scan(tmp_dir, report_name)
        
        # 按仓库分组
        gitleaks_by_repo = group_by_repo_gitleaks(gitleaks_result)
        semgrep_by_repo = group_by_repo_semgrep(semgrep_result)
        
        all_repos = set(gitleaks_by_repo.keys()) | set(semgrep_by_repo.keys())
        known_repos = {"bdo-biz-archive", "bdo-pm-file", "bdo-pm-report", "bdo-project-manage"}
        
        lines.append("扫描说明：对 7 个涉及仓库做了 gitleaks（密钥）+ semgrep（安全规则）扫描。")
        lines.append("")
        lines.append("### 1) gitleaks（密钥/凭证泄露）")
        lines.append("")
        
        for repo in sorted(known_repos & all_repos):
            findings = gitleaks_by_repo.get(repo, [])
            if findings:
                lines.append(f"**{repo}：{len(findings)} 条**")
                for finding in findings:
                    rule = finding.get("RuleID", "unknown")
                    file_path = finding.get("File", "unknown")
                    start_line = finding.get("StartLine", "?")
                    match = finding.get("Match", "")[:30] + "..." if len(finding.get("Match", "")) > 30 else finding.get("Match", "")
                    lines.append(f"- {rule}：{file_path} 第 {start_line} 行（匹配：{match}）")
            else:
                lines.append(f"**{repo}：0 条**")
        
        other_repos = all_repos - known_repos
        other_count = sum(len(gitleaks_by_repo.get(r, [])) for r in other_repos)
        lines.append(f"**其他项目：{other_count} 条**")
        lines.append("")
        
        lines.append("### 2) semgrep（安全规则）")
        lines.append("")
        
        for repo in sorted(known_repos & all_repos):
            findings = semgrep_by_repo.get(repo, [])
            if findings:
                error_count = sum(1 for f in findings if f.get("extra", {}).get("severity", f.get("severity", "WARNING")) == "ERROR")
                warning_count = len(findings) - error_count
                prefix = ""
                if error_count > 0 and warning_count > 0:
                    prefix = f"（ERROR {error_count} / WARNING {warning_count}）"
                elif error_count > 0:
                    prefix = f"（ERROR {error_count}）"
                elif warning_count > 0:
                    prefix = f"（WARNING {warning_count}）"
                
                lines.append(f"**{repo}：{len(findings)} 条{prefix}**")
                
                # 按规则分组
                rules_by_type: Dict[str, Dict[str, Any]] = {}
                for finding in findings:
                    metadata = finding.get("extra", {}).get("metadata", {})
                    semgrep_rule = metadata.get("semgrep.dev", {}).get("rule", {})
                    rule_id = semgrep_rule.get("rule_id", "unknown")
                    rule_desc = metadata.get("semgrep.dev", {}).get("rule", {}).get("description", finding.get("extra", {}).get("message", ""))
                    if rule_id not in rules_by_type:
                        rules_by_type[rule_id] = {"desc": rule_desc, "count": 0, "examples": []}
                    rules_by_type[rule_id]["count"] += 1
                    if len(rules_by_type[rule_id]["examples"]) < 2:
                        file_path = finding.get("path", "unknown")
                        start_line = finding.get("start", {}).get("line", "?")
                        rules_by_type[rule_id]["examples"].append(f"{file_path} 第 {start_line} 行")
                
                for rule_id, data in sorted(rules_by_type.items(), key=lambda x: x[1]["count"], reverse=True):
                    lines.append(f"- `{rule_id}` {data['desc']}（{data['count']} 条）")
                    for ex in data["examples"][:2]:
                        lines.append(f"  - {ex}")
            else:
                lines.append(f"**{repo}：0 条**")
        
        other_semgrep = [f for r in other_repos for f in semgrep_by_repo.get(r, [])]
        if other_semgrep:
            lines.append(f"**其他项目：{len(other_semgrep)} 条**")
        else:
            lines.append("**其他项目：0 条**")
    else:
        lines.append("（安全扫描需集成 gitleaks/semgrep，当前报告仅基于元数据）")
    lines.append("")

    # 工时比例总结
    lines.append("#### 工时比例总结")
    if daily_total_hours > 0:
        ratio_hours = combined_h / daily_total_hours
        if ratio_hours < 0.5:
            lines.append(f"- **提示**：估算投入仅为填报工时的 {ratio_hours*100:.0f}%（{ratio_hours:.2f}x），可能存在日报填报工时偏高或遗漏提交的情况")
        elif ratio_hours > 1.5:
            lines.append(f"- **提示**：估算投入为填报工时的 {ratio_hours:.1f}x（{ratio_hours*100:.0f}%），可能存在未填报的开发活动")
        else:
            lines.append(f"- 工时比例合理（估算/填报：{ratio_hours:.2f}x，即 {ratio_hours*100:.0f}%）")
    else:
        lines.append("- 无日报记录，无法计算工时比例")
    lines.append("")

    lines.append("## 五、结论与建议")
    lines.append("")
    if combined_h > 8:
        lines.append("- **交付强度**：本周高强度交付，注意代码质量和休息间隔")
    elif combined_h > 4:
        lines.append("- **交付强度**：本周中等强度交付，节奏稳定")
    else:
        lines.append("- **交付强度**：本周低强度交付，建议确认任务完成状态")

    lines.append("")
    lines.append("- **改进建议**：")
    lines.append("  - 保持提交粒度适中，避免过大或过小")
    lines.append("  - 提交信息中关联禅道任务ID（格式：#任务号）")
    lines.append("  - 高风险代码（path-traversal、DES弃用等）请优先整改")
    lines.append("")

    # Write
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return output_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gitlab-json", required=True, help="Path to gitlab_weekly_*.json")
    ap.add_argument("--zentao-json", required=True, help="Path to zentao_weekly_*.json")
    ap.add_argument("--users-file", required=True, help="Path to users.txt")
    ap.add_argument("--out-dir", help="Output directory. If omitted, write to skills/pms-week/logs/")

    args = ap.parse_args()

    git_data = load_json(args.gitlab_json)
    zt_data = load_json(args.zentao_json)

    users = load_users(args.users_file)

    out_dir = args.out_dir
    if not out_dir:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs"))
        os.makedirs(base_dir, exist_ok=True)
        out_dir = base_dir

    try:
        from_str = git_data.get("date_range", {}).get("from_iso", "")
        until_str = git_data.get("date_range", {}).get("until_iso", "")
        
        if not from_str:
            from_str = git_data.get("date_range", {}).get("from", "unknown")
        if not until_str:
            until_str = git_data.get("date_range", {}).get("to", "unknown")
        
        if "T" in from_str and ("+" in from_str or from_str.endswith("Z")):
            from_dt = dt.fromisoformat(from_str).astimezone(timezone(timedelta(hours=8)))
            until_dt = dt.fromisoformat(until_str).astimezone(timezone(timedelta(hours=8)))
        else:
            from_dt = dt.fromisoformat(from_str).replace(tzinfo=timezone(timedelta(hours=8)))
            until_dt = dt.fromisoformat(until_str).replace(tzinfo=timezone(timedelta(hours=8)))
        
        from_date = from_dt.strftime("%Y-%m-%d")
        until_date = until_dt.strftime("%Y-%m-%d")
        folder_name = from_date.replace("-", "")
    except Exception as e:
        from_date = "unknown"
        until_date = "unknown"
        folder_name = "unknown"
        print(f"Date parsing warning: {e}", file=sys.stderr)

    out_dir = os.path.join(out_dir, folder_name)
    os.makedirs(out_dir, exist_ok=True)

    generated = []
    for username, realname in users.items():
        try:
            if not git_data.get("users", {}).get(username) and not zt_data.get("users", {}).get(username):
                continue

            out_path = os.path.join(out_dir, f"{realname}_{from_date}_{until_date}_week.md")
            generate_markdown_report(username, realname, git_data, zt_data, out_path)
            generated.append(out_path)
        except Exception as e:
            print(f"Failed {username}: {e}", file=sys.stderr)

    print(f"Generated {len(generated)} reports in {out_dir}")
    for p in generated:
        print(f"  - {p}")
    return 0


if __name__ == "__main__":
    import argparse
    from datetime import datetime as dt
    raise SystemExit(main())
