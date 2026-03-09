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
  - **Preferred:** GitLab Personal Access Token (PAT) with `read_api` (and `read_repository` if fetching diffs/files)
  - Or a project/group deploy token if allowed
- Scope of report:
  - Group(s) or project(s)
  - Date (default: today in Asia/Shanghai) and work window (e.g. 09:00-19:00)
- Identity mapping:
  - GitLab username ↔ real name (if needed for reporting)

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
   Minimum checks (fast, no repo clone needed if patch available):
   - Secret patterns: AWS keys, generic API keys, private keys, tokens in code/config
   - Dangerous calls/patterns (language dependent): `eval`, `exec`, shell injection, deserialization, SQL concat
   - Dependency risk hints: lockfile changes, version downgrades, new network-facing libs
   - Test signal: changes in core modules without test updates

   Optional (if user has infra and agrees): integrate dedicated tools (gitleaks, semgrep) by cloning repos.

5. **Generate report**
   - Per developer:
     - Summary bullets (what/where)
     - Time estimate + confidence (low/med/high)
     - Risk findings (severity + evidence pointers)
   - Team summary:
     - Total activity, biggest risky changes, blockers

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

- `scripts/gitlab_daily.py`: fetch activity + produce JSON/Markdown
- `scripts/risk_scan.py`: scan patches/text for secrets + heuristics
- `references/gitlab_api.md`: API endpoints and query patterns

Read these files when implementing or debugging.
