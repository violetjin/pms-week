#!/usr/bin/env python3
"""User mapping helper.

Supports users.txt lines in format:
  account|name
Example:
  zhu.junfang|朱君芳

Provides fuzzy lookup by Chinese name (substring match) or by account.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass
class User:
    account: str
    name: str


def load_users(path: str) -> List[User]:
    users: List[User] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if "|" in s:
                a, n = s.split("|", 1)
                users.append(User(a.strip(), n.strip()))
            else:
                users.append(User(s, ""))
    return users


def build_indexes(users: List[User]) -> Tuple[Dict[str, User], List[User]]:
    by_account = {u.account: u for u in users if u.account}
    return by_account, users


def resolve(query: str, users: List[User]) -> List[User]:
    q = query.strip()
    if not q:
        return []
    by_account, all_users = build_indexes(users)

    # exact account
    if q in by_account:
        return [by_account[q]]

    # exact name
    exact = [u for u in all_users if u.name and u.name == q]
    if exact:
        return exact

    # substring fuzzy for name
    fuzzy = [u for u in all_users if u.name and q in u.name]
    return fuzzy


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--users-file", required=True)
    ap.add_argument("--query", required=True, help="account or chinese name")
    args = ap.parse_args()

    users = load_users(args.users_file)
    matches = resolve(args.query, users)
    for u in matches:
        print(f"{u.account}\t{u.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
