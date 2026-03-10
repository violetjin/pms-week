#!/usr/bin/env python3
"""Generate per-developer daily report from GitLab.

This script is intended as a reusable primitive for the OpenClaw skill.

It supports:
- Fetch commits for projects within a time window
- Group by author
- Estimate time by session heuristic and churn heuristic
- Produce JSON and (optional) markdown

Usage (example):
  python3 gitlab_daily.py \
    --base-url https://gitlab.example.com \
    --token $GITLAB_TOKEN \
    --group sacp --group lxits \
    --users-file users.txt \
    --from 2026-03-01 --to 2026-03-09 --tz Asia/Shanghai \
    --work-start 09:00 --work-end 19:00 \
    --out report.json

Notes:
- Token may be omitted if using env var GITLAB_TOKEN.
- Keep output token-free.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None  # type: ignore

import urllib.request
import urllib.parse


def http_get_json(url: str, token: str, timeout: int = 30) -> Tuple[Any, Dict[str, str]]:
    req = urllib.request.Request(url)
    req.add_header("PRIVATE-TOKEN", token)
    req.add_header("User-Agent", "openclaw-gitlab-code-daily/1.0")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8")
        headers = {k: v for k, v in resp.headers.items()}
        return json.loads(body), headers


def paged_get(url: str, token: str) -> List[Any]:
    items: List[Any] = []
    page = 1
    while True:
        sep = "&" if "?" in url else "?"
        page_url = f"{url}{sep}per_page=100&page={page}"
        data, headers = http_get_json(page_url, token)
        if isinstance(data, list):
            items.extend(data)
        else:
            raise ValueError(f"Expected list response for {page_url}")

        next_page = headers.get("X-Next-Page", "")
        if not next_page:
            break
        page = int(next_page)
        time.sleep(0.1)
    return items


def parse_hhmm(s: str) -> dt.time:
    m = re.fullmatch(r"(\d{2}):(\d{2})", s)
    if not m:
        raise ValueError(f"Invalid HH:MM: {s}")
    hh, mm = int(m.group(1)), int(m.group(2))
    return dt.time(hour=hh, minute=mm)


def local_window_to_utc(date_str: str, tz: str, start_hhmm: str, end_hhmm: str) -> Tuple[str, str]:
    if ZoneInfo is None:
        raise RuntimeError("zoneinfo not available; use Python 3.9+")
    z = ZoneInfo(tz)
    d = dt.date.fromisoformat(date_str)
    start = dt.datetime.combine(d, parse_hhmm(start_hhmm), tzinfo=z)
    end = dt.datetime.combine(d, parse_hhmm(end_hhmm), tzinfo=z)
    if end <= start:
        end = end + dt.timedelta(days=1)
    start_utc = start.astimezone(dt.timezone.utc).isoformat()
    end_utc = end.astimezone(dt.timezone.utc).isoformat()
    return start_utc, end_utc


@dataclass
class Commit:
    project_id: int
    project_name: str
    sha: str
    title: str
    authored_date: str
    author_name: str
    author_email: str
    additions: int = 0
    deletions: int = 0
    total: int = 0
    web_url: str = ""

    def authored_dt(self) -> dt.datetime:
        return dt.datetime.fromisoformat(self.authored_date.replace("Z", "+00:00"))


def fetch_project(base_api: str, token: str, project_id: int) -> Dict[str, Any]:
    url = f"{base_api}/projects/{project_id}"
    data, _ = http_get_json(url, token)
    return data


def discover_group_projects(base_api: str, token: str, group: str) -> List[int]:
    # group can be numeric id or full path; for full path must be URL-encoded
    g_enc = urllib.parse.quote(group, safe="")
    url = f"{base_api}/groups/{g_enc}/projects?include_subgroups=true"
    projs = paged_get(url, token)
    ids: List[int] = []
    for p in projs:
        try:
            ids.append(int(p.get("id")))
        except Exception:
            pass
    return ids


def fetch_commits(base_api: str, token: str, project_id: int, since_iso: str, until_iso: str) -> List[Dict[str, Any]]:
    url = f"{base_api}/projects/{project_id}/repository/commits?since={urllib.parse.quote(since_iso)}&until={urllib.parse.quote(until_iso)}"
    return paged_get(url, token)


def fetch_commit_detail(base_api: str, token: str, project_id: int, sha: str) -> Dict[str, Any]:
    url = f"{base_api}/projects/{project_id}/repository/commits/{sha}"
    data, _ = http_get_json(url, token)
    return data


def estimate_sessions(commits: List[Commit], gap_minutes: int = 90, pad_minutes: int = 20) -> float:
    if not commits:
        return 0.0
    commits_sorted = sorted(commits, key=lambda c: c.authored_dt())
    gap = dt.timedelta(minutes=gap_minutes)
    pad = dt.timedelta(minutes=pad_minutes)

    total = dt.timedelta(0)
    session_start = commits_sorted[0].authored_dt()
    last = session_start

    for c in commits_sorted[1:]:
        t = c.authored_dt()
        if t - last > gap:
            total += (last - session_start) + pad
            session_start = t
        last = t

    total += (last - session_start) + pad
    hours = max(0.0, total.total_seconds() / 3600.0)
    return hours


def estimate_churn(commits: List[Commit], loc_per_hour: int = 200, min_hours: float = 0.25, max_hours: float = 10.0) -> float:
    churn = sum(c.total for c in commits)
    h = churn / float(loc_per_hour) if loc_per_hour > 0 else 0.0
    h = max(min_hours if churn > 0 else 0.0, min(max_hours, h))
    return h


def load_user_map(path: str) -> Dict[str, str]:
    """Return account->name map from users.txt supporting 'account|name' lines."""
    m: Dict[str, str] = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
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


def resolve_users(allow_map: Dict[str, str], queries: List[str]) -> List[str]:
    """Resolve provided user queries (account or chinese name fuzzy) into accounts."""
    accounts = list(allow_map.keys())
    resolved: List[str] = []
    for q in queries:
        q = q.strip()
        if not q:
            continue
        if q in allow_map:
            resolved.append(q)
            continue
        # exact chinese name
        exact = [a for a, n in allow_map.items() if n and n == q]
        if exact:
            resolved.extend(exact)
            continue
        # fuzzy substring in chinese name
        fuzzy = [a for a, n in allow_map.items() if n and q in n]
        resolved.extend(fuzzy)
    # de-dup preserve order
    out: List[str] = []
    seen = set()
    for a in resolved:
        if a not in seen:
            out.append(a)
            seen.add(a)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True, help="GitLab base URL, e.g. https://gitlab.example.com")
    ap.add_argument("--token", default=os.environ.get("GITLAB_TOKEN", ""), help="GitLab token (or env GITLAB_TOKEN)")
    ap.add_argument("--project-id", action="append", type=int, help="Project id (repeatable). If omitted, use --group to discover projects")
    ap.add_argument("--group", action="append", default=[], help="Group full path or numeric id (repeatable), used to discover all projects")
    ap.add_argument("--users-file", help="Allowlist file. Supports lines: 'account' or 'account|name'")
    ap.add_argument("--user", action="append", default=[], help="User query to include (repeatable). Accepts account or Chinese name (fuzzy)")
    ap.add_argument("--from", dest="date_from", required=True, help="YYYY-MM-DD (inclusive)")
    ap.add_argument("--to", dest="date_to", required=True, help="YYYY-MM-DD (inclusive)")
    ap.add_argument("--tz", default="Asia/Shanghai")
    ap.add_argument("--work-start", default="09:00")
    ap.add_argument("--work-end", default="19:00")
    ap.add_argument("--session-gap-min", type=int, default=90)
    ap.add_argument("--session-pad-min", type=int, default=20)
    ap.add_argument("--loc-per-hour", type=int, default=200)
    ap.add_argument("--out", help="Output path. If omitted, write to skills/gitlab-code-daily/logs/")

    args = ap.parse_args()
    if not args.token:
        print("Missing --token or env GITLAB_TOKEN", file=sys.stderr)
        return 2

    # Default output path under skill logs
    if not args.out:
        import os
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs"))
        os.makedirs(base_dir, exist_ok=True)
        suffix = "_".join(sorted(set(args.user))) if args.user else "all"
        args.out = os.path.join(base_dir, f"gitlab_daily_{args.date_from}_{args.date_to}_{suffix}.json")

    base_api = args.base_url.rstrip("/") + "/api/v4"
    # Resolve date range into UTC window [from 00:00 local .. to+1 00:00 local) but keep work window per-day when bucketing.
    date_from = dt.date.fromisoformat(args.date_from)
    date_to = dt.date.fromisoformat(args.date_to)
    if date_to < date_from:
        raise SystemExit("--to must be >= --from")

    # For API commit fetch we query whole day ranges; later we keep only those inside the work window per day.
    since_iso, _ = local_window_to_utc(args.date_from, args.tz, "00:00", "23:59")
    _, until_iso = local_window_to_utc((date_to + dt.timedelta(days=1)).isoformat(), args.tz, "00:00", "00:01")

    commits_by_user: Dict[str, List[Commit]] = collections.defaultdict(list)

    # Load allowed usernames
    allow_map: Dict[str, str] = {}
    if args.users_file:
        allow_map = load_user_map(args.users_file)

    if not allow_map:
        raise SystemExit("Empty allowlist; check --users-file")

    # If --user provided, resolve (account or chinese name fuzzy); otherwise include all in allowlist.
    if args.user:
        resolved = resolve_users(allow_map, args.user)
        if not resolved:
            raise SystemExit(f"No users matched queries: {args.user}")
        allow_users = set(resolved)
    else:
        allow_users = set(allow_map.keys())

    project_ids: List[int] = []
    if args.project_id:
        project_ids.extend(args.project_id)

    if args.group:
        # Discover projects under groups
        for g in args.group:
            project_ids.extend(discover_group_projects(base_api, args.token, g))

    project_ids = sorted(set(project_ids))
    if not project_ids:
        raise SystemExit("No projects selected; pass --project-id or --group")

    for pid in project_ids:
        proj = fetch_project(base_api, args.token, pid)
        pname = proj.get("path_with_namespace", str(pid))
        raw_commits = fetch_commits(base_api, args.token, pid, since_iso, until_iso)
        for rc in raw_commits:
            sha = rc.get("id")
            detail = fetch_commit_detail(base_api, args.token, pid, sha)
            stats = detail.get("stats") or {}

            # Map to username using your convention: username@bdo.com.cn
            username = ""
            author_email = (detail.get("author_email") or rc.get("author_email") or "").strip().lower()
            if author_email.endswith("@bdo.com.cn"):
                username = author_email.split("@", 1)[0]

            c = Commit(
                project_id=pid,
                project_name=pname,
                sha=sha,
                title=detail.get("title") or rc.get("title") or "",
                authored_date=detail.get("authored_date") or rc.get("authored_date") or rc.get("created_at"),
                author_name=detail.get("author_name") or rc.get("author_name") or "",
                author_email=detail.get("author_email") or rc.get("author_email") or "",
                additions=int(stats.get("additions") or 0),
                deletions=int(stats.get("deletions") or 0),
                total=int(stats.get("total") or 0),
                web_url=detail.get("web_url") or "",
            )

            # Filter to work-window per day
            adt_local = c.authored_dt().astimezone(ZoneInfo(args.tz)) if ZoneInfo else c.authored_dt()
            if not (date_from <= adt_local.date() <= date_to):
                continue
            ws = parse_hhmm(args.work_start)
            we = parse_hhmm(args.work_end)
            t = adt_local.time()
            if not (ws <= t <= we):
                continue

            if username not in allow_users:
                continue

            commits_by_user[username].append(c)
        time.sleep(0.1)

    report: Dict[str, Any] = {
        "date_range": {"from": args.date_from, "to": args.date_to},
        "tz": args.tz,
        "window": {"since_utc": since_iso, "until_utc": until_iso, "work_start": args.work_start, "work_end": args.work_end},
        "users": {},
    }

    for username in sorted(allow_users):
        commits = commits_by_user.get(username, [])
        session_h = estimate_sessions(commits, args.session_gap_min, args.session_pad_min)
        churn_h = estimate_churn(commits, args.loc_per_hour)
        combined_h = max(session_h, churn_h)
        loc_total = sum(c.total for c in commits)
        report["users"][username] = {
            "username": username,
            "name": allow_map.get(username, ""),
            "counts": {"commits": len(commits), "loc_total": loc_total},
            "estimates_hours": {"session": round(session_h, 2), "churn": round(churn_h, 2), "combined": round(combined_h, 2)},
            "efficiency": {
                "loc_per_hour": round((loc_total / combined_h), 2) if combined_h > 0 else 0.0,
                "commits_per_hour": round((len(commits) / combined_h), 2) if combined_h > 0 else 0.0,
            },
            "commits": [c.__dict__ for c in sorted(commits, key=lambda x: x.authored_dt())],
        }

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
