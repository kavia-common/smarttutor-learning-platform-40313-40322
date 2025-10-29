#!/usr/bin/env python
"""
Run backend smoke checks from repository root.
- Ensures backend .env exists (copy from example if missing)
- Runs alembic upgrade head
- Starts server briefly and checks /health
"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BACKEND = ROOT / "smarttutor-learning-platform-40313-40322" / "flask_backend"

def main() -> int:
    if not BACKEND.exists():
        print("Backend path not found:", BACKEND, file=sys.stderr)
        return 1
    os.chdir(BACKEND)

    # Ensure .env exists
    env_file = BACKEND / ".env"
    if not env_file.exists():
        example = BACKEND / ".env.example"
        if example.exists():
            env_file.write_text(example.read_text())
            print("Created flask_backend/.env from .env.example (update values for non-dev).")

    # Upgrade DB (best-effort if DATABASE_URL is present)
    try:
        if os.getenv("DATABASE_URL", ""):
            subprocess.check_call(["alembic", "upgrade", "head"])
        else:
            print("DATABASE_URL not set; skipping alembic upgrade.")
    except Exception as e:
        print("WARNING: alembic upgrade failed:", e)

    # Run smoke health
    return subprocess.call([sys.executable, "scripts/smoke_health.py"])

if __name__ == "__main__":
    raise SystemExit(main())
