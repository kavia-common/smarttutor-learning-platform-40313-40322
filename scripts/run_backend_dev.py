#!/usr/bin/env python
"""
Run the Flask backend in development mode from repository root.
"""
import os
import sys
from pathlib import Path

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    backend = root / "smarttutor-learning-platform-40313-40322" / "flask_backend"
    if not backend.exists():
        print("Backend folder not found:", backend, file=sys.stderr)
        return 2
    os.chdir(str(backend))
    os.environ.setdefault("FLASK_ENV", "development")
    # Use run_dev.py to start
    from run_dev import main as run
    run()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
