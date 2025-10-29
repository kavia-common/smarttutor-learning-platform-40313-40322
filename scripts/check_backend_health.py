#!/usr/bin/env python
"""
CI health check for the Flask backend.
- GET /health
- GET /openapi.json
- Optionally check /diag/ping
"""
import json
import sys
import urllib.request

BASE = "http://localhost:8000"

def fetch(path: str):
    with urllib.request.urlopen(BASE + path, timeout=8) as resp:
        data = resp.read().decode("utf-8")
        ctype = resp.headers.get("Content-Type", "")
        return resp.status, ctype, data

def main() -> int:
    ok = True
    try:
        status, ctype, data = fetch("/health")
        print("GET /health:", status, ctype)
        if status != 200:
            ok = False
    except Exception as e:
        print("ERROR fetching /health:", e)
        ok = False

    try:
        status, ctype, data = fetch("/openapi.json")
        print("GET /openapi.json:", status, ctype)
        if status != 200:
            ok = False
        else:
            try:
                json.loads(data)
            except Exception:
                print("ERROR: /openapi.json is not valid JSON")
                ok = False
    except Exception as e:
        print("ERROR fetching /openapi.json:", e)
        ok = False

    try:
        status, ctype, data = fetch("/diag/ping")
        print("GET /diag/ping:", status, ctype)
        if status != 200:
            ok = False
    except Exception as e:
        print("WARN: /diag/ping not available:", e)

    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
