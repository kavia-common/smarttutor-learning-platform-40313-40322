#!/usr/bin/env python
"""
Print Alembic current head information, and optionally stamp to head if env var DO_STAMP_HEAD=1.
"""
import os
import subprocess

def main() -> int:
    try:
        print("== Alembic current ==")
        subprocess.check_call(["alembic", "current"])
        print("== Alembic heads ==")
        subprocess.check_call(["alembic", "heads"])
    except subprocess.CalledProcessError as e:
        return e.returncode

    if os.getenv("DO_STAMP_HEAD") == "1":
        print("Stamping database to head...")
        try:
            subprocess.check_call(["alembic", "stamp", "head"])
            print("Stamped to head.")
        except subprocess.CalledProcessError as e:
            return e.returncode
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
