---
name: pms-week
description: Generate weekly development reports by correlating GitLab commits with ZenTao task records.
---

# pms-week

## What this skill does

- Fetch weekly activity per developer from GitLab (commits/merge requests)
- Fetch weekly task records from ZenTao (禅道) via direct SQL queries
- Correlate code changes with task assignments to assess consistency
- Output per-developer weekly reports under `logs/`

This skill is designed for **on-prem/self-hosted GitLab** and **direct MySQL access to ZenTao**.

## Required inputs (implicit via configuration)

- GitLab base URL: `https://gitlab.bdo.com.cn`
- ZenTao MySQL connection (env vars: `ZENTAO_DB_HOST/PORT/USER/PASS/NAME`)
- Users file: `references/users.txt` (all developers with account|name mapping)
- Groups: all projects (no group filter)

## Workflow

1. **Collect GitLab activity**
   - Fetch commits for all projects across all groups (discovered via `groups.txt` or default)
   - Filter by developer accounts in `users.txt`
   - Date range: last Monday 00:00 to Sunday 24:00 (Asia/Shanghai)

2. **Fetch ZenTao tasks**
   - Direct SQL query to `bdo_zentao.bdo_zt_main_task`
   - Filter by developer (realname) and date range (begin_time)
   - Aggregate by developer

3. **Correlate & analyze**
   - For each developer, compare:
     - GitLab commits (files/modules + intent)
     - ZenTao tasks (system name, task title, classify)
   - Report consistency flag: "high"/"medium"/"low"
   - Flag: commits without matching tasks, or tasks without commits
   - Compute section-6 system score card with these weights:
     - 交付活跃度：2.0
     - 任务一致性：2.0
     - 工时合理性：4.0
     - 风险质量：2.0
   - 工时合理性按估算/填报比例单边分档：
     - 高于或等于 0.8：4.0 分
     - 0.6 ~ 0.8：3.0 分
     - 0.4 ~ 0.6：2.0 分
     - 0.2 ~ 0.4：1.0 分
     - 低于 0.2：0.5 分

4. **Output**
   - `logs/开发人员_YYYY-MM-DD_YYYY-MM-DD_week.md`
   - JSON raw data for audit

## Bundled resources

- `scripts/run_weekly.py`: main weekly pipeline entrypoint
- `scripts/fetch_gitlab_weekly.py`: fetch commits (wrapper of gitlab_daily.py logic)
- `scripts/fetch_zentao_weekly.py`: direct SQL query to ZenTao
- `scripts/analyze_weekly.py`: correlate commits vs tasks, generate markdown report
- `scripts/generate_weekly_summary.py`: generate weekly summary from the dated log directory
- `scripts/bak/`: inactive or backup scripts not used by the current `run_weekly.py` flow
- `references/users.txt`: developer mapping (account|name)
- `references/groups.txt`: allowlist groups (optional; if absent, fetch all)
- `references/sql_templates/`: ZenTao query templates

## Environment variables

- `GITLAB_TOKEN`: GitLab Personal Access Token (read_api + read_repository)
- `ZENTAO_DB_HOST` (default: `172.17.10.55`)
- `ZENTAO_DB_PORT` (default: `5188`)
- `ZENTAO_DB_USER` (default: `openclaw`)
- `ZENTAO_DB_PASS` (default: `openclaw@123`)
- `ZENTAO_DB_NAME` (default: `bdo_zentao`)

> Tokens and DB credentials should be stored in environment, never in code.

## Output template (per person)

```markdown
# 开发人员周报（GitLab + 禅道）

- 人员：姓名（account）
- 时间范围：YYYY-MM-DD ~ YYYY-MM-DD（上周一 00:00 - 周日 24:00）
- 覆盖范围：所有项目

## 一、GitLab 提交概览
- 提交次数：N commits
- 代码变更量：X LOC
- 估算投入：Y 小时
- 效率指标：LOC/h, commits/h

## 二、禅道任务概览
- 任务数：N
- 分类分布：用户需求/内部需求/生产BUG/...
- 系统分布：XXX系统、YYY系统

## 三、一致性分析
- 一致性评分：high/medium/low
- 提交内容与任务匹配度说明
- 异常标记：提交无对应任务 / 任务无提交

## 四、风险提示
- 密钥/安全扫描结果（如 gitleaks/semgrep）
- 提交粒度、高频小提交等质量信号

## 五、结论与建议
- 本周交付重点
- 改进建议
```

## Run command (cron example)

```bash
# 每周一 00:00 运行
0 0 * * 1 cd /path/to/openclaw/workspace && python3 -m skills.pms-week.run_weekly
```