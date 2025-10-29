#!/usr/bin/env python
"""
Run the Flask backend via Gunicorn from repository root (dev convenience).
Requires 'gunicorn' to be installed in the current Python environment.

Usage:
  python scripts/run_backend_gunicorn.py
"""
import os
import sys
from pathlib import Path
import subprocess

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    backend = root / "smarttutor-learning-platform-40313-40322" / "flask_backend"
    if not backend.exists():
        print("Backend folder not found:", backend, file=sys.stderr)
        return 2
    os.chdir(str(backend))
    cmd = ["gunicorn", "-b", "0.0.0.0:8000", "-w", "2", "wsgi:app"]
    try:
        return subprocess.call(cmd)
    except FileNotFoundError:
        print("gunicorn not found. Install it or use: python run_dev.py", file=sys.stderr)
        return 127

if __name__ == "__main__":
    raise SystemExit(main())
