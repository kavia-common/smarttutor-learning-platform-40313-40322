#!/usr/bin/env python
"""
Ensure an initial Alembic migration exists; create one if missing.
"""
import os
import subprocess
from pathlib import Path

def main() -> int:
    versions_dir = Path("migrations/versions")
    versions_dir.mkdir(parents=True, exist_ok=True)
    existing = list(versions_dir.glob("*.py"))
    if existing:
        print("Migration(s) already exist:", ", ".join(p.name for p in existing))
        return 0
    print("No migrations found. Creating initial autogenerate migration...")
    try:
        subprocess.check_call(["alembic", "revision", "--autogenerate", "-m", "initial"])
        print("Initial migration created.")
        return 0
    except subprocess.CalledProcessError as e:
        print("Failed to create migration:", e)
        return e.returncode

if __name__ == "__main__":
    raise SystemExit(main())
