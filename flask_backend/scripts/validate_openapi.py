#!/usr/bin/env python
"""
Fetch /openapi.json and validate essential fields exist.
"""
import json
import sys
import urllib.request

def fetch(base: str):
    url = f"{base.rstrip('/')}/openapi.json"
    with urllib.request.urlopen(url, timeout=6) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    try:
        spec = fetch(base)
    except Exception as e:
        print("Failed to fetch OpenAPI:", e)
        return 2
    required = ["openapi", "info", "paths"]
    missing = [k for k in required if k not in spec]
    if missing:
        print("OpenAPI invalid, missing keys:", ", ".join(missing))
        return 3
    print("OpenAPI ok. Title:", spec.get("info", {}).get("title"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
