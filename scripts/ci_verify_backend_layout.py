#!/usr/bin/env python
"""
Verify that the flask_backend layout contains core files and folders.

This is a quick CI/helper script that prints a simple status table and returns non-zero if critical files are missing.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
BACKEND = ROOT / "smarttutor-learning-platform-40313-40322" / "flask_backend"

REQUIRED = [
    BACKEND / "app" / "__init__.py",
    BACKEND / "app" / "config.py",
    BACKEND / "app" / "db.py",
    BACKEND / "app" / "models" / "__init__.py",
    BACKEND / "migrations" / "env.py",
    BACKEND / "migrations" / "versions" / "0001_initial.py",
    BACKEND / "requirements.txt",
    BACKEND / ".env.example",
    BACKEND / "wsgi.py",
]

def exists(p: Path) -> bool:
    try:
        return p.exists()
    except Exception:
        return False

def main() -> int:
    print("Verifying backend layout at:", BACKEND)
    missing = []
    for p in REQUIRED:
        ok = exists(p)
        print(f"[{'OK' if ok else 'MISS'}] {p.relative_to(ROOT)}")
        if not ok:
            missing.append(p)
    if missing:
        print(f"Missing {len(missing)} critical file(s).")
        return 1
    print("Backend layout verification OK.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
