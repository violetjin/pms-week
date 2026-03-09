#!/usr/bin/env python3
"""Lightweight risk scan for code changes.

Input: a JSON report produced by gitlab_daily.py OR a list of patches/text.
Output: findings with severity and evidence pointers.

This is intentionally heuristic and fast. For higher fidelity, integrate semgrep/gitleaks.
"""

from __future__ import annotations

import argparse
import json
import re
from typing import Any, Dict, List, Tuple


SECRET_PATTERNS: List[Tuple[str, re.Pattern, str]] = [
    ("aws_access_key_id", re.compile(r"AKIA[0-9A-Z]{16}"), "high"),
    ("aws_secret_access_key", re.compile(r"(?i)aws(.{0,20})?secret(.{0,20})?key\s*[:=]\s*['\"]?[0-9a-zA-Z/+]{30,}['\"]?"), "high"),
    ("private_key", re.compile(r"-----BEGIN (RSA|EC|OPENSSH|DSA) PRIVATE KEY-----"), "high"),
    ("generic_token", re.compile(r"(?i)(token|apikey|api_key|secret)\s*[:=]\s*['\"][^'\"]{16,}['\"]"), "med"),
]

DANGEROUS_PATTERNS: List[Tuple[str, re.Pattern, str]] = [
    ("python_eval", re.compile(r"\beval\s*\("), "med"),
    ("python_exec", re.compile(r"\bexec\s*\("), "med"),
    ("js_eval", re.compile(r"\beval\s*\("), "med"),
    ("java_runtime_exec", re.compile(r"Runtime\.getRuntime\(\)\.exec\("), "med"),
    ("deserialization", re.compile(r"(?i)ObjectInputStream|pickle\.loads\(|yaml\.load\("), "med"),
]


def scan_text(text: str) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []
    for name, pat, sev in SECRET_PATTERNS:
        for m in pat.finditer(text):
            findings.append({"type": "secret", "rule": name, "severity": sev, "match": m.group(0)[:80]})
    for name, pat, sev in DANGEROUS_PATTERNS:
        for m in pat.finditer(text):
            findings.append({"type": "pattern", "rule": name, "severity": sev, "match": m.group(0)[:80]})
    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="Input JSON file")
    ap.add_argument("--out", required=True, help="Output JSON file")
    args = ap.parse_args()

    with open(args.inp, "r", encoding="utf-8") as f:
        data = json.load(f)

    # This scanner expects optional fields in commit dicts (like patches). If absent, it will only flag based on metadata.
    out: Dict[str, Any] = {"date": data.get("date"), "authors": {}}

    for author_key, author in (data.get("authors") or {}).items():
        author_findings: List[Dict[str, Any]] = []
        for c in author.get("commits", []):
            # If future version stores diff/patch snippets, scan them here.
            patch = c.get("patch") or ""
            if patch:
                fs = scan_text(patch)
                for fnd in fs:
                    fnd["project"] = c.get("project_name")
                    fnd["sha"] = c.get("sha")
                author_findings.extend(fs)

            # Metadata-only heuristics
            title = (c.get("title") or "").lower()
            if "hotfix" in title or "revert" in title:
                author_findings.append({"type": "meta", "rule": "risky_title", "severity": "low", "match": c.get("title"), "sha": c.get("sha"), "project": c.get("project_name")})

        out["authors"][author_key] = {"findings": author_findings}

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
