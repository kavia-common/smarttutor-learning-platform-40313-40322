#!/usr/bin/env python
"""
CI readiness check for Flask backend.

- Verifies .env or env has DATABASE_URL and JWT_SECRET
- Tries to hit /health and /api/status if server is running (optional)
"""
import os
import sys
import urllib.request
from dotenv import load_dotenv

def fetch(url: str) -> int:
    try:
        with urllib.request.urlopen(url, timeout=3) as r:
            return r.getcode()
    except Exception:
        return -1

def main() -> int:
    load_dotenv()
    ok = True
    if not os.getenv("DATABASE_URL"):
        print("ERROR: DATABASE_URL not set")
        ok = False
    if not os.getenv("JWT_SECRET"):
        print("ERROR: JWT_SECRET not set")
        ok = False

    port = os.getenv("PORT", "8000")
    base = f"http://127.0.0.1:{port}"
    health = fetch(f"{base}/health")
    status = fetch(f"{base}/api/status")
    print(f"/health -> {health}")
    print(f"/api/status -> {status}")
    # Do not fail if endpoints are not reachable (server may not be running in CI step)
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
