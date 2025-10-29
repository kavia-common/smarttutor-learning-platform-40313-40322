#!/usr/bin/env python
"""
Run Alembic from the flask_backend directory, regardless of current working dir.
Usage:
  python smarttutor-learning-platform-40313-40322/flask_backend/scripts/alembic_here.py upgrade head
"""
import os
import sys
import subprocess
from pathlib import Path

def main() -> int:
    here = Path(__file__).resolve().parent.parent
    cmd = ["alembic"] + sys.argv[1:]
    print("==> (cd {}) {}".format(here, " ".join(cmd)))
    return subprocess.call(cmd, cwd=str(here))

if __name__ == "__main__":
    raise SystemExit(main())
