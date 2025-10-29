#!/usr/bin/env python
"""
Unified diagnostics CLI for SmartTutor backend.

Usage:
  python scripts/diagnostics_cli.py [base_url]
Runs:
  - env-check
  - alembic-info
  - verify_models
  - table_counts
  - smoke_basic
"""
import subprocess
import sys
from pathlib import Path

BASE = "http://localhost:8000"

def run(cmd):
    print(f"-> {cmd}")
    return subprocess.call(cmd, shell=True)

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else BASE
    here = Path(__file__).resolve().parent.parent
    cmds = [
        "python scripts/check_env_vars.py",
        "python scripts/alembic_info.py",
        "python scripts/verify_models.py",
        "python scripts/table_counts.py",
        f"python scripts/smoke_basic.py {base}",
        f"python scripts/validate_openapi.py {base}",
    ]
    failures = 0
    for c in cmds:
        rc = run(c)
        if rc != 0:
            failures += 1
    if failures:
        print(f"Diagnostics finished with {failures} failure(s).")
        return 1
    print("Diagnostics finished successfully.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
