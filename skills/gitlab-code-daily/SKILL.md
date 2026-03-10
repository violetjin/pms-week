---
name: gitlab-code-daily
description: Generate per-developer daily reports from a self-hosted GitLab based on commits/merge requests, estimate time spent from code changes and activity windows, and flag potential code risks (secrets, unsafe patterns, low test coverage, risky deps). Use when you need automated daily reports, GitLab commit log analysis, change-size/time estimation, or lightweight code-risk scanning for internal R&D teams.
---

# GitLab Code Daily

## What this skill does

- Pull daily activity per user from GitLab (commits and optionally merge requests)
- Summarize what each person did (files/modules + intent)
- Estimate time spent (heuristic; configurable)
- Run code-risk checks (secrets + simple heuristics; optional pluggable scanners)
- Output a per-person daily report and a team summary

This skill is designed for **on-prem/self-hosted GitLab**.

## Required inputs (ask user if missing)

- GitLab base URL, e.g. `https://gitlab.example.com`
- Access method:
  - GitLab Personal Access Token (PAT) with `read_api` and `read_repository` (needed for diffs and repo clone)
- Scope of report:
  - **All projects** (discover via groups list or an allowlist)
  - Date range (YYYY-MM-DD..YYYY-MM-DD) and work window (e.g. 09:00-19:00)
  - Target users (GitLab usernames)
- Identity mapping:
  - GitLab **username** is the primary key; optionally map username → display name

Never print tokens in logs or reports.

## Workflow

1. **Collect activity**
   - For each target project (or group projects), list commits within the date range.
   - Attribute commits to users by `author_email` / `author_name` / `committer` / `user` fields (prefer GitLab user when available).
   - Optionally include MRs created/merged/commented.

2. **Enrich**
   - Fetch commit detail and diff stats (files changed, additions/deletions).
   - Optionally fetch patches for limited-size commits for risk scanning.

3. **Estimate time** (heuristics; choose one and state it in report)
   - **Session window heuristic (recommended):** bucket commits into sessions per developer using an inactivity gap (e.g. 90 minutes). Session duration = (last_commit - first_commit) + clamp padding (e.g. 20m).
   - **Change-size heuristic:** map churn to time via configurable rates, e.g. 1h per 200 LOC changed, with min/max caps.
   - Combine: `max(session_estimate, churn_estimate*weight)` or report both.

4. **Risk scan**
   Languages: Java / Python / JavaScript / HTML.

   Minimum checks (fast, no repo clone needed if patch available):
   - Secret patterns: AWS keys, generic API keys, private keys, tokens in code/config
   - Dangerous calls/patterns (language dependent): `eval`, `exec`, shell injection, deserialization, SQL concat
   - Dependency risk hints: lockfile changes, version downgrades, new network-facing libs
   - Test signal: changes in core modules without test updates

   Integrate dedicated tools by cloning repos:
   - **gitleaks** for secrets
   - **semgrep** for code patterns (Java/Python/JS)

5. **Efficiency & quality metrics**
   Provide per-user metrics over a date range:
   - Output: commits count, MR count (optional), LOC churn, active days
   - Time estimate: session/churn/combined
   - Efficiency: churn per hour, commits per hour (heuristic), cycle-time proxy (if MR data enabled)
   - Quality: risk findings counts by severity; tests-touched ratio (if repo clone); revert/hotfix ratio

6. **Generate report (default artifacts)**

   When the user requests "get <person> commits in <date range> and analyze", always generate these artifacts under `skills/gitlab-code-daily/logs/`:

   - `XXX_daily.md`: personal daily-style analysis report (efficiency + quality summary)
   - `XXX_remediation.md`: remediation checklist (file/line + evidence + commit sha)

   Also keep the raw JSON used for analysis.

   Report content:
   - Per developer:
     - Summary bullets (what/where)
     - Time estimate + confidence (low/med/high)
     - Risk findings (severity + evidence pointers)
     - Remediation items with file/line and commit sha (use `git blame`)

## Output templates

### Per-person daily report (markdown)

- 姓名/账号：<name> (<gitlab_username>)
- 日期：YYYY-MM-DD
- 今日提交概览：
  - <module/file>: <intent>
- 估算投入：<X> 小时（方法：session/churn/combined；置信度：low/med/high）
- 风险提示：
  - [high|med|low] <finding>（证据：<project> <commit_sha> <file:line or path>）
- 明日计划/待跟进（如可推断，谨慎）：
  - <optional>

### Team summary

- 覆盖范围：<groups/projects>
- 今日总提交：N commits / M MRs
- 估算总投入：T 小时
- Top 风险：
  - ...

## Bundled resources

- `scripts/gitlab_daily.py`: fetch activity + produce JSON
- `scripts/user_map.py`: resolve Chinese name ↔ account from `users.txt`
- `scripts/risk_scan.py`: scan patches/text for secrets + heuristics (optional)
- `references/gitlab_api.md`: API endpoints and query patterns
- `references/users.txt`: allowlist (supports `account|name`)

Read these files when implementing or debugging.
