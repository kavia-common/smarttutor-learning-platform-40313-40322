#!/usr/bin/env python
"""
Run Alembic upgrade head via Python in CI or local dev.
"""
import subprocess
import sys

def main() -> int:
    try:
        return subprocess.call(["alembic", "upgrade", "head"])
    except FileNotFoundError:
        print("Alembic not found. Install dependencies first: pip install -r requirements.txt", file=sys.stderr)
        return 127

if __name__ == "__main__":
    raise SystemExit(main())
