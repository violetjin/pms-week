---
name: wecom-webhook
description: Send messages to a WeCom/WeChat Work (企业微信) group robot webhook URL (qyapi.weixin.qq.com/cgi-bin/webhook/send?key=...). Use when the user asks to push notifications/reports (e.g., daily AI news summary) to a WeCom webhook.
---

# WeCom webhook sender

Use the bundled script to POST a text/markdown message to a WeCom group robot webhook.

## Send markdown (preferred)

```bash
python3 "$OPENCLAW_WORKSPACE/skills/wecom-webhook/scripts/send_wecom_webhook.py" \
  --url "<WEBHOOK_URL>" \
  --msgtype markdown \
  --text "<MARKDOWN_CONTENT>"
```

## Send plain text

```bash
python3 "$OPENCLAW_WORKSPACE/skills/wecom-webhook/scripts/send_wecom_webhook.py" \
  --url "<WEBHOOK_URL>" \
  --msgtype text \
  --text "<TEXT_CONTENT>"
```

## Notes

- Keep messages concise; WeCom robots have length limits.
- If you need to include links, include full URLs.
- The script prints the response body; success typically returns JSON with `errcode: 0`.
