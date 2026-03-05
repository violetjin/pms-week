#!/usr/bin/env python3
"""Send a message to a WeCom (企业微信) group robot webhook.

Usage:
  send_wecom_webhook.py --url <webhook_url> --text <text> [--msgtype text|markdown]

Notes:
- WeCom group robots support msgtype: text, markdown (and others).
- This script uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request


def post_json(url: str, payload: dict, timeout: float = 10.0) -> tuple[int, str]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        return resp.getcode(), body


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True, help="WeCom webhook URL")
    ap.add_argument("--text", required=True, help="Message text/markdown")
    ap.add_argument("--msgtype", default="markdown", choices=["text", "markdown"], help="WeCom msgtype")
    ap.add_argument("--timeout", type=float, default=10.0, help="HTTP timeout seconds")
    args = ap.parse_args()

    if args.msgtype == "text":
        payload = {"msgtype": "text", "text": {"content": args.text}}
    else:
        payload = {"msgtype": "markdown", "markdown": {"content": args.text}}

    code, body = post_json(args.url, payload, timeout=args.timeout)
    print(body)

    # WeCom returns JSON like: {"errcode":0,"errmsg":"ok"}
    try:
        j = json.loads(body)
        if int(j.get("errcode", 1)) != 0:
            return 2
    except Exception:
        # non-json: treat as failure
        return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
