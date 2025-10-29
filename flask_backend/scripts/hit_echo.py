#!/usr/bin/env python
"""
Call /api/echo with optional JSON body and print response.
Usage:
  python scripts/hit_echo.py [base_url] [json_body]
Examples:
  python scripts/hit_echo.py
  python scripts/hit_echo.py http://localhost:8000 '{"hello":"world"}'
"""
import json
import sys
import urllib.request

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    url = f"{base.rstrip('/')}/api/echo"
    body = None
    if len(sys.argv) > 2:
        body = sys.argv[2].encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST" if body else "GET")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=5) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print(json.dumps(data, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
