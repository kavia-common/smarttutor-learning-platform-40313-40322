#!/usr/bin/env python
"""
Check core diagnostics endpoints for HTTP 200 and JSON responses.
"""
import json
import sys
import urllib.request

CORE_ENDPOINTS = [
    "/health",
    "/api/status",
    "/api/version",
    "/api/routes",
    "/api/uptime",
    "/api/memory",
    "/api/proc",
    "/api/cpu",
    "/api/time",
    "/api/headers",
    "/openapi.json",
]

def fetch_json(url: str):
    with urllib.request.urlopen(url, timeout=8) as resp:
        body = resp.read().decode("utf-8")
        return resp.status, json.loads(body)

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    failures = 0
    for ep in CORE_ENDPOINTS:
        url = f"{base.rstrip('/')}{ep}"
        try:
            status, data = fetch_json(url)
            ok = 200 <= status < 300
            print(f"{'OK' if ok else 'FAIL'} {status} {ep} :: keys={list(data)[:4]}")
            if not ok:
                failures += 1
        except Exception as e:
            print(f"FAIL {ep}: {e}")
            failures += 1
    return 0 if failures == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
