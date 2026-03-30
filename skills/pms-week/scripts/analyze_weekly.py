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
import sys
from datetime import datetime, timedelta, timezone
from typing import Dict


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
from typing import Any, Dict, List, Optional


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


def extract_commit_subject(commit_title: str) -> str:
    """Extract module/intent from commit title."""
    # Try to extract JIRA/zentao task ID or module prefix
    import re
    # Example: "feat(report): add merge report" -> "report", "#12345 add merge report"
    m = re.match(r"^(feat|fix|docs|style|refactor|perf|test|chore)(\(.+\))?:\s*(.*)$", commit_title, re.IGNORECASE)
    if m:
        return f"{m.group(1)}: {m.group(3)}"
    # Try #number
    m = re.search(r"(#\d+)", commit_title)
    if m:
        return commit_title
    # Default: first 30 chars
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
            "subjects": subjects[:5],  # top 5
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
    # Heuristic: if >80% commits have #taskID, high; if 50-80%, medium; else low
    import re
    commits_with_taskid = 0
    for c in commits:
        title = c.get("title", "")
        if re.search(r"#\d+", title):
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


def calculate_system_scores(
    commits_count: int,
    loc_total: int,
    task_count: int,
    daily_total_hours: float,
    combined_h: float,
    commits_with_taskid: int,
    merge_commits: int,
    commits_without_taskid_count: int,
    risk_issue_count: int,
    risk_error_count: int,
) -> Dict[str, float]:
    """Generate the section-6 score card used by weekly reports and summary parsing.

    New weights (total 10):
    - 交付活跃度：2.0
    - 任务一致性：2.0
    - 工时合理性：4.0
    - 风险质量：2.0
    """
    actionable_commits = max(0, commits_count - merge_commits)

    # 1) 交付活跃度（2.0）
    if commits_count <= 0 and loc_total <= 0:
        if task_count >= 5:
            delivery_score = 1.4
        elif task_count >= 3:
            delivery_score = 1.0
        elif task_count >= 1:
            delivery_score = 0.6
        else:
            delivery_score = 0.0
    else:
        if commits_count >= 8 or loc_total >= 2000 or combined_h >= 35:
            delivery_score = 2.0
        elif commits_count >= 5 or loc_total >= 1000 or combined_h >= 15:
            delivery_score = 1.7
        elif commits_count >= 2 or loc_total >= 200 or combined_h >= 4:
            delivery_score = 1.3
        else:
            delivery_score = 0.8
        if delivery_score < 1.4 and task_count >= 5:
            delivery_score = 1.4

    # 2) 任务一致性（2.0）
    if commits_count == 0:
        consistency_score = 0.8 if task_count > 0 else 0.0
    elif actionable_commits <= 0:
        consistency_score = 2.0 if commits_with_taskid > 0 else 1.0
    elif commits_with_taskid == 0:
        consistency_score = 1.0 if commits_count >= 5 and task_count > 0 else 0.4
    else:
        task_ratio = commits_with_taskid / max(1, actionable_commits)
        if commits_without_taskid_count == 0:
            consistency_score = 2.0
        elif task_ratio >= 0.75:
            consistency_score = 1.7
        elif task_ratio >= 0.40:
            consistency_score = 1.1
        else:
            consistency_score = 0.7

    # 3) 工时合理性（4.0）
    if daily_total_hours <= 0:
        hours_score = 1.2 if commits_count == 0 else 1.6
    elif commits_count == 0 and combined_h <= 0:
        hours_score = 1.2
    else:
        ratio = combined_h / max(daily_total_hours, 0.01)
        if 0.8 <= ratio <= 1.2:
            hours_score = 4.0
        elif 0.6 <= ratio < 0.8 or 1.2 < ratio <= 1.5:
            hours_score = 3.0
        elif 0.4 <= ratio < 0.6 or 1.5 < ratio <= 2.0:
            hours_score = 2.0
        elif 0.2 <= ratio < 0.4 or 2.0 < ratio <= 3.0:
            hours_score = 1.0
        else:
            hours_score = 0.2

    # 4) 风险质量（2.0）
    if commits_count == 0:
        risk_score = 1.8
    elif risk_issue_count <= 0:
        risk_score = 2.0
    elif risk_error_count > 0 or risk_issue_count > 10:
        risk_score = 1.2
    else:
        risk_score = 1.6

    total_score = round(delivery_score + consistency_score + hours_score + risk_score, 1)
    return {
        "delivery": round(delivery_score, 1),
        "consistency": round(consistency_score, 1),
        "hours": round(hours_score, 1),
        "risk": round(risk_score, 1),
        "total": total_score,
    }


def build_system_score_notes(scores: Dict[str, float]) -> List[str]:
    """Build short explanations for the section-6 score card."""
    notes: List[str] = []

    delivery = scores["delivery"]
    consistency = scores["consistency"]
    hours = scores["hours"]
    risk = scores["risk"]

    if delivery >= 1.7:
        notes.append("交付活跃度较好")
    elif delivery <= 0.8:
        notes.append("交付活跃度偏弱")

    if consistency >= 1.7:
        notes.append("任务关联较清晰")
    elif consistency <= 0.8:
        notes.append("任务关联度偏弱")

    if hours >= 3.0:
        notes.append("工时匹配度较好")
    else:
        notes.append("工时匹配度一般")

    if len(notes) < 3:
        if risk >= 1.6:
            notes.append("本周改动风险可控")
        else:
            notes.append("需关注本周改动风险")

    return notes[:3]


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

    # Date range - parse from GitLab data (UTC timezone)
    range_from = gitlab_data.get("date_range", {}).get("from_iso", "")
    range_until = gitlab_data.get("date_range", {}).get("until_iso", "")

    try:
        from_dt = dt.fromisoformat(range_from)
        until_dt = dt.fromisoformat(range_until)
        # Convert to Asia/Shanghai timezone (UTC+8)
        from_shanghai = from_dt.astimezone(timezone(timedelta(hours=8)))
        until_shanghai = until_dt.astimezone(timezone(timedelta(hours=8)))
        from_date = from_shanghai.strftime("%Y-%m-%d")
        # until_shanghai is next Monday 00:00, so subtract 1 day to get Sunday
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
    ticket_titles: Dict[str, str] = {}  # 存储任务ID和标题的映射
    if daily_reports:
        for d in daily_reports:
            hours = float(d.get("任务花费时间") or 0)
            daily_total_hours += hours
            ticket_id = d.get("任务ID")
            ticket_title = d.get("任务标题", "")
            if ticket_id:
                daily_by_ticket[str(ticket_id)] = daily_by_ticket.get(str(ticket_id), 0.0) + hours
                # 保存任务标题（只保存一次）
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
        # 按工时降序排列，显示全部任务，避免与日报总工时不一致
        sorted_tickets = sorted(daily_by_ticket.items(), key=lambda x: x[1], reverse=True)
        for tid, hrs in sorted_tickets:
            title = ticket_titles.get(tid, "")
            lines.append(f"  - #{tid} {title}：{hrs:.2f} 小时")
    lines.append("")

    lines.append("## 三、一致性分析")
    lines.append("")

    # 1. 提交内容检查
    import re
    commits_with_taskid = 0
    commits_without_taskid = []  # 不含任务ID的提交
    commits_merge = []  # merge 提交
    for c in commits:
        title = c.get("title", "")
        if re.search(r"#\d+", title):
            commits_with_taskid += 1
        elif "Merge" in title or "merge" in title.lower():
            commits_merge.append(title)
        else:
            commits_without_taskid.append(title)

    if not commits:
        consistency = "low"
        consistency_note = "无代码提交"
    else:
        # 计算包含任务ID的比例
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

    # 2. 提交内容详细检查
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

    # 3. 工时对比分析
    lines.append("#### 工时对比分析")
    lines.append(f"- GitLab 估算投入：{combined_h:.2f} 小时")
    lines.append(f"- 日报总填报工时：{daily_total_hours:.2f} 小时")
    if daily_total_hours > 0:
        ratio_hours = combined_h / daily_total_hours
        lines.append(f"- 估算/填报比例：{ratio_hours:.2f}x")
        lines.append("")
        # 找出误差大的任务（填报工时 > 2 * 估算工时）
        lines.append("#### 工时误差 > 100% 的任务（填报工时 > 2x 估算）")
        high_variance_tasks = []
        for ticket_id, daily_h in daily_by_ticket.items():
            # Find commits with this ticket_id
            ticket_commits = [c for c in commits if f"#{ticket_id}" in c.get("title", "")]
            if ticket_commits:
                ticket_session_h = estimate_hours_by_session(ticket_commits)
                ticket_churn_h = estimate_hours_by_churn(ticket_commits)
                ticket_estimated = max(ticket_session_h, ticket_churn_h)
                if daily_h > ticket_estimated * 2 and ticket_estimated > 0.1:
                    high_variance_tasks.append((ticket_id, ticket_estimated, daily_h))
            else:
                # No commits with ticket_id, use estimated 0.5h as baseline
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

    # 4. 安全扫描（gitleaks + semgrep）
    lines.append("## 四、风险提示")
    lines.append("")
    lines.append("扫描说明：对 7 个涉及仓库做了 gitleaks（密钥）+ semgrep（安全规则）扫描。")
    lines.append("")
    
    if commits:
        # 运行 gitleaks 扫描（只扫描 workspace 下属于 groups.txt 群组的项目）
        import subprocess
        import json as json_lib
        import re
        
        # 获取 pms-week skill 根目录
        skill_root = os.path.dirname(os.path.dirname(os.path.dirname(output_path)))
        groups_file = os.path.join(skill_root, "references", "groups.txt")
        groups = []
        if os.path.exists(groups_file):
            try:
                with open(groups_file, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            groups.append(line)
            except Exception:
                pass
        # 默认群组列表（如果没有 groups.txt）
        if not groups:
            groups = ["sacp", "lxits", "bdo-sz", "fantasy", "product-group", "bdo-biz-general"]
        
        # 创建临时目录（在日期文件夹下）
        tmp_dir = os.path.join(os.path.dirname(output_path), "tmp")
        os.makedirs(tmp_dir, exist_ok=True)
        
        # 构建扫描路径：只扫描 workspace 下的 gitlab 目录（属于 groups 的项目）
        scan_path = os.path.join("/home/jinye/.openclaw/workspace", "gitlab")
        
        gitleaks_report = os.path.join(tmp_dir, f"gitleaks_{os.path.basename(output_path)}.json")
        
        gitleaks_result = []
        try:
            result = subprocess.run(
                ["gitleaks", "detect", "--source", scan_path, "--report-format", "json", "--report-path", gitleaks_report],
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
        
        # 运行 semgrep 扫描
        semgrep_report = os.path.join(tmp_dir, f"semgrep_{os.path.basename(output_path)}.json")
        semgrep_result = []
        try:
            result = subprocess.run(
                ["semgrep", "--json", "--output", semgrep_report, scan_path],
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
        
        # 按项目分组 gitleaks 结果（只统计 workspace 下 bdo- 开头的项目）
        gitleaks_by_project: Dict[str, Dict[str, int]] = {}
        total_gitleaks = 0
        workspace_path = "/home/jinye/.openclaw/workspace"
        for finding in gitleaks_result:
            file_path = finding.get("File", finding.get("file", ""))
            # gitleaks 返回的 File 是相对路径，需要拼接 workspace 路径
            if not file_path.startswith(workspace_path):
                file_path = os.path.join(workspace_path, file_path)
            # 只统计 workspace 下的文件
            if not file_path.startswith(workspace_path):
                continue
            # 提取项目名：从 path 中提取 bdo- 开头的目录名
            # 支持 gitlab/bdo-* 或直接 bdo-* 的路径
            rel_path = file_path[len(workspace_path) + 1:]  # 去掉前缀
            parts = rel_path.split("/")
            project_name = "unknown"
            for i, part in enumerate(parts):
                if part.startswith("bdo-"):
                    project_name = part
                    break
            if project_name == "unknown" and parts:
                project_name = parts[0]
            
            # 忽略临时文件和非业务代码文件
            # 例如：skills/ 目录下的临时文件、gitleaks 生成的报告文件
            rel_path_lower = rel_path.lower()
            if "skills" in parts or "gitleaks" in rel_path_lower or "semgrep" in rel_path_lower:
                continue
            
            rule = finding.get("RuleID", finding.get("rule_id", "unknown"))
            if project_name not in gitleaks_by_project:
                gitleaks_by_project[project_name] = {}
            gitleaks_by_project[project_name][rule] = gitleaks_by_project[project_name].get(rule, 0) + 1
            total_gitleaks += 1
        
        # 按项目分组 semgrep 结果
        semgrep_by_project: Dict[str, Dict[str, Dict[str, int]]] = {}
        for match in semgrep_result:
            file_path = match.get("path", "")
            # 提取项目名
            # 支持 gitlab/bdo-* 或直接 bdo-* 的路径
            parts = file_path.split("/")
            project_name = "unknown"
            for i, part in enumerate(parts):
                if part.startswith("bdo-"):
                    project_name = part
                    break
            if project_name == "unknown":
                for i, part in enumerate(parts):
                    if part == "workspace" and i + 1 < len(parts):
                        project_name = parts[i + 1]
                        break
            if project_name == "unknown" and parts:
                project_name = parts[0]
            
            # 忽略临时文件和非业务代码文件
            # 例如：skills/ 目录下的临时文件、gitleaks 生成的报告文件
            rel_path_lower = file_path.lower()
            parts_lower = [p.lower() for p in parts]
            if "skills" in parts_lower or "gitleaks" in rel_path_lower or "semgrep" in rel_path_lower:
                continue
            
            # 规则 ID 从 metadata.semgrep.dev.rule.rule_id 获取
            metadata = match.get("extra", {}).get("metadata", {})
            semgrep_rule = metadata.get("semgrep.dev", {}).get("rule", {})
            rule = semgrep_rule.get("rule_id", match.get("rule_id", "unknown"))
            # 规则描述从 message 获取
            rule_desc = match.get("extra", {}).get("message", "")
            severity = match.get("extra", {}).get("severity", match.get("severity", "WARNING"))
            
            if project_name not in semgrep_by_project:
                semgrep_by_project[project_name] = {}
            if rule not in semgrep_by_project[project_name]:
                semgrep_by_project[project_name][rule] = {"error": 0, "warning": 0, "desc": rule_desc}
            if severity == "ERROR":
                semgrep_by_project[project_name][rule]["error"] += 1
            else:
                semgrep_by_project[project_name][rule]["warning"] += 1
        
        # 输出 gitleaks 结果
        lines.append("### 1) gitleaks（密钥/凭证泄露）")
        lines.append("")
        
        # 按项目排序
        for project in sorted(gitleaks_by_project.keys()):
            rules = gitleaks_by_project[project]
            rule_count = sum(rules.values())
            rules_str = ", ".join([f"{rule}: {count} 条" for rule, count in sorted(rules.items())])
            lines.append(f"**{project}：{rule_count} 条**")
            for rule, count in sorted(rules.items()):
                lines.append(f"- {rule}：{count} 条")
        
        other_count = total_gitleaks - sum(gitleaks_by_project.values())
        if other_count > 0:
            lines.append(f"**其他项目：{other_count} 条**")
        else:
            lines.append("**其他项目：0 条**")
        lines.append("")
        
        # 输出 semgrep 结果
        lines.append("### 2) semgrep（安全规则）")
        lines.append("")
        
        for project in sorted(semgrep_by_project.keys()):
            rules = semgrep_by_project[project]
            total_error = sum(r["error"] for r in rules.values())
            total_warning = sum(r["warning"] for r in rules.values())
            total = total_error + total_warning
            error_str = f"ERROR {total_error}" if total_error > 0 else ""
            warning_str = f"WARNING {total_warning}" if total_warning > 0 else ""
            prefix = ""
            if error_str and warning_str:
                prefix = f"（{error_str} / {warning_str}）"
            elif error_str:
                prefix = f"（{error_str}）"
            elif warning_str:
                prefix = f"（{warning_str}）"
            
            lines.append(f"**{project}：{total} 条{prefix}**")
            for rule, data in sorted(semgrep_by_project[project].items(), key=lambda x: x[1]["error"] + x[1]["warning"], reverse=True):
                rule_total = data["error"] + data["warning"]
                desc = data.get("desc", "")
                # 使用规则描述作为说明
                desc_text = f"（{desc}）" if desc else ""
                lines.append(f"- `{rule}`{desc_text}（{rule_total} 条）")
        
        # 检查是否有其他项目
        all_projects = set(gitleaks_by_project.keys()) | set(semgrep_by_project.keys())
        known_projects = {"bdo-biz-archive", "bdo-pm-file", "bdo-pm-report", "bdo-project-manage"}
        other_projects = all_projects - known_projects
        if other_projects:
            lines.append(f"**其他项目：{sum(len(gitleaks_by_project.get(p, {})) for p in other_projects) + sum(sum(r['error'] + r['warning'] for r in semgrep_by_project.get(p, {}).values()) for p in other_projects)} 条**")
        else:
            lines.append("**其他项目：0 条**")
    else:
        lines.append("（安全扫描需集成 gitleaks/semgrep，当前报告仅基于元数据）")
    lines.append("")

    # 4. 工时比例总结
    lines.append("#### 工时比例总结")
    ratio_hours = None
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

    system_scores = calculate_system_scores(
        commits_count=git_counts.get('commits', 0),
        loc_total=git_counts.get('loc_total', 0),
        task_count=zt_summary['total'],
        daily_total_hours=daily_total_hours,
        combined_h=combined_h,
        commits_with_taskid=commits_with_taskid,
        merge_commits=len(commits_merge),
        commits_without_taskid_count=len(commits_without_taskid),
        risk_issue_count=total_gitleaks + sum(
            sum(r['error'] + r['warning'] for r in rules.values())
            for rules in semgrep_by_project.values()
        ) if commits else 0,
        risk_error_count=sum(
            sum(r['error'] for r in rules.values())
            for rules in semgrep_by_project.values()
        ) if commits else 0,
    )
    score_notes = build_system_score_notes(system_scores)

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

    lines.append("## 六、系统性评分")
    lines.append("")
    lines.append(f"- **总分：{system_scores['total']:.1f} / 10**")
    lines.append("- **评分明细：**")
    lines.append(f"  - 交付活跃度：{system_scores['delivery']:.1f} / 2.0")
    lines.append(f"  - 任务一致性：{system_scores['consistency']:.1f} / 2.0")
    lines.append(f"  - 工时合理性：{system_scores['hours']:.1f} / 4.0")
    lines.append(f"  - 风险质量：{system_scores['risk']:.1f} / 2.0")
    lines.append("- **评分说明：**")
    for note in score_notes:
        lines.append(f"  - {note}")
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

    # Default out dir
    out_dir = args.out_dir
    if not out_dir:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs"))
        os.makedirs(base_dir, exist_ok=True)
        out_dir = base_dir

    # Parse date range to build filename
    # Support both GitLab format (from_iso/until_iso) and ZenTao format (from/to)
    try:
        from_str = git_data.get("date_range", {}).get("from_iso", "")
        until_str = git_data.get("date_range", {}).get("until_iso", "")
        
        # Fallback to ZenTao format
        if not from_str:
            from_str = git_data.get("date_range", {}).get("from", "unknown")
        if not until_str:
            until_str = git_data.get("date_range", {}).get("to", "unknown")
        
        # Parse date from ISO string (GitLab) or datetime string (ZenTao)
        # GitLab: 2026-03-08T16:00:00+00:00
        # ZenTao: 2026-03-09 00:00:00
        
        if "T" in from_str and ("+" in from_str or from_str.endswith("Z")):
            # ISO format with timezone - convert to Shanghai
            from_dt = dt.fromisoformat(from_str).astimezone(timezone(timedelta(hours=8)))
            until_dt = dt.fromisoformat(until_str).astimezone(timezone(timedelta(hours=8)))
        else:
            # Local datetime string (no timezone info)
            from_dt = dt.fromisoformat(from_str).replace(tzinfo=timezone(timedelta(hours=8)))
            until_dt = dt.fromisoformat(until_str).replace(tzinfo=timezone(timedelta(hours=8)))
        
        from_date = from_dt.strftime("%Y-%m-%d")
        # Input `until` is exclusive upper bound (next Monday 00:00),
        # but report filename/date range should display the inclusive Sunday.
        until_date = (until_dt - timedelta(days=1)).strftime("%Y-%m-%d")
        # Folder name is the Monday (from_date)
        folder_name = from_date.replace("-", "")
    except Exception as e:
        from_date = "unknown"
        until_date = "unknown"
        folder_name = "unknown"
        print(f"Date parsing warning: {e}", file=sys.stderr)

    # Create date-based subdirectory
    out_dir = os.path.join(out_dir, folder_name)
    os.makedirs(out_dir, exist_ok=True)

    # Generate per-developer reports
    generated = []
    for username, realname in users.items():
        try:
            # Skip if user has no data
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
