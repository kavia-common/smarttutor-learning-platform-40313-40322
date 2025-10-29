#!/usr/bin/env python
"""
Initialize the database by applying all Alembic migrations.

Usage:
  python init_db.py
"""
import subprocess
import sys
from dotenv import load_dotenv

def main() -> int:
    load_dotenv()
    try:
        # Run alembic upgrade head
        result = subprocess.run([sys.executable, "manage.py", "upgrade", "head"], check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Failed to initialize DB: {e}")
        return e.returncode or 1

if __name__ == "__main__":
    raise SystemExit(main())
