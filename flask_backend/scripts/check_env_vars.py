#!/usr/bin/env python
"""
Check required environment variables for backend.
"""
import os
import sys

REQUIRED = ["DATABASE_URL", "JWT_SECRET"]

def main() -> int:
    missing = [k for k in REQUIRED if not os.getenv(k)]
    if missing:
        print("Missing environment variables:", ", ".join(missing))
        return 1
    print("All required environment variables are set.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
