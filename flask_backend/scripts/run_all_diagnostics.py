#!/usr/bin/env python
"""
Run a set of diagnostics against a running backend instance.
Usage: python scripts/run_all_diagnostics.py [base_url]
"""
import json
import sys
import urllib.request

BASE = "http://localhost:8000"

def get(base: str, path: str):
    url = f"{base.rstrip('/')}{path}"
    with urllib.request.urlopen(url, timeout=6) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else BASE
    checks = [
        "/health",
        "/api/status",
        "/api/version",
        "/api/uptime",
        "/api/memory",
        "/api/metrics",
        "/api/proc",
        "/api/cpu",
        "/api/routes",
        "/openapi.json",
    ]
    failures = 0
    for path in checks:
        try:
            data = get(base, path)
            print(f"OK {path}: {list(data)[:3]} ...")
        except Exception as e:
            print(f"FAIL {path}: {e}")
            failures += 1
    if failures:
        print(f"Diagnostics completed with {failures} failures")
        return 1
    print("Diagnostics completed successfully")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
