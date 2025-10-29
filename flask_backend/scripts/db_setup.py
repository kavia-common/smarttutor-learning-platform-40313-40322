#!/usr/bin/env python
"""
One-shot database setup:
- verifies env vars
- runs alembic upgrade head
- runs seed.py (optional with --seed)
Usage:
  python scripts/db_setup.py [--seed]
"""
import argparse
import os
import subprocess
import sys

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", action="store_true", help="Run seed.py after migration")
    args = parser.parse_args()

    missing = [k for k in ("DATABASE_URL", "JWT_SECRET") if not os.getenv(k)]
    if missing:
        print("Missing env:", ", ".join(missing))
        return 2

    try:
        subprocess.check_call(["alembic", "upgrade", "head"])
    except subprocess.CalledProcessError as e:
        print("Migration failed:", e)
        return e.returncode

    if args.seed:
        try:
            subprocess.check_call([sys.executable, "seed.py"])
        except subprocess.CalledProcessError as e:
            print("Seed failed:", e)
            return e.returncode

    print("Database setup complete.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
