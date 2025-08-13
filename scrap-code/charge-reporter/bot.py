#!/usr/bin/env python3
"""
bot.py

Run from cron (e.g. every 5 minutes). No suppression — script exits after one check.

Requirements:
    pip install requests

Provide TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID as environment variables, or pass via --token and --chat.
"""
import subprocess
import re
import os
import sys
import argparse
import json
from pathlib import Path

try:
    import requests
except Exception:
    print("Missing dependency: requests. Install with: pip install requests", file=sys.stderr)
    sys.exit(2)

RE_ACPI = re.compile(r"Battery\s*(\d+):\s*(\w+),\s*(\d+)%")

def run_acpi():
    try:
        out = subprocess.run(["acpi"], capture_output=True, text=True, check=False)
    except FileNotFoundError:
        return None
    return out.stdout.strip()

def parse_acpi(output):
    items = []
    for line in output.splitlines():
        m = RE_ACPI.search(line)
        if m:
            idx = int(m.group(1))
            status = m.group(2)
            pct = int(m.group(3))
            items.append({"name": f"Battery{idx}", "status": status, "pct": pct, "raw": line})
    return items

def read_sysfs_batteries():
    base = Path("/sys/class/power_supply")
    if not base.exists():
        return []
    out = []
    for p in base.iterdir():
        cap = p / "capacity"
        stat = p / "status"
        if cap.exists() and stat.exists():
            try:
                pct = int(cap.read_text().strip())
                status = stat.read_text().strip()
                out.append({"name": p.name, "status": status, "pct": pct, "raw": f"{p.name}: {status}, {pct}%"})
            except Exception:
                continue
    return out

def gather_batteries():
    acpi_out = run_acpi()
    if acpi_out:
        parsed = parse_acpi(acpi_out)
        if parsed:
            return parsed
    return read_sysfs_batteries()

def send_telegram(token, chat_id, text, parse_mode=None):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    if parse_mode:
        payload["parse_mode"] = parse_mode
    r = requests.post(url, json=payload, timeout=10)
    r.raise_for_status()
    data = r.json()
    if not data.get("ok"):
        raise RuntimeError(f"Telegram API returned error: {data}")

def main():
    parser = argparse.ArgumentParser(description="Notify Telegram group when battery low/high (run once).")
    parser.add_argument("--token", help="Telegram bot token (or set TELEGRAM_BOT_TOKEN env var)")
    parser.add_argument("--chat", help="Telegram chat id (or set TELEGRAM_CHAT_ID env var)")
    parser.add_argument("--low", type=int, default=20, help="Low threshold percent (default 20)")
    parser.add_argument("--high", type=int, default=90, help="High threshold percent (default 90)")
    args = parser.parse_args()

    token = args.token or os.getenv("TELEGRAM_BOT_TOKEN")
    chat = args.chat or os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat:
        print("Telegram token and chat id must be provided via env vars or --token/--chat", file=sys.stderr)
        sys.exit(2)

    bats = gather_batteries()
    if not bats:
        print("No battery info found (acpi not present and /sys fallback empty).", file=sys.stderr)
        sys.exit(0)

    low_hits = []
    high_hits = []
    for b in bats:
        st = b["status"].lower()
        pct = int(b["pct"])
        if "discharging" in st and pct < args.low:
            low_hits.append((b["name"], pct, b["raw"]))
        if "charging" in st and pct > args.high:
            high_hits.append((b["name"], pct, b["raw"]))

    try:
        if low_hits:
            lines = ["*Battery low* (discharging):"]
            for name, pct, raw in low_hits:
                lines.append(f"- {name}: {pct}% — `{raw}`")
            msg = "\n".join(lines)
            send_telegram(token, chat, msg, parse_mode="Markdown")
            print("Sent low-battery message.")
        if high_hits:
            lines = ["*Battery high/near-full while charging*:"]
            for name, pct, raw in high_hits:
                lines.append(f"- {name}: {pct}% — `{raw}`")
            msg = "\n".join(lines)
            send_telegram(token, chat, msg, parse_mode="Markdown")
            print("Sent high-battery message.")
    except Exception as e:
        print("Failed to send Telegram message:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
