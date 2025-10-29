#!/usr/bin/env python
import os
import subprocess
from pathlib import Path

def sh(cmd: str):
    print(f"==> {cmd}")
    subprocess.check_call(cmd, shell=True)

def main():
    root = Path(__file__).resolve().parent
    os.chdir(root)
    # Ensure .env exists
    subprocess.call("python scripts/bootstrap_env.py", shell=True)
    # Upgrade DB to latest migration
    sh("alembic upgrade head")
    # Run app
    env = os.environ.copy()
    env.setdefault("PORT", "8000")
    subprocess.check_call("python wsgi.py", shell=True, env=env)

if __name__ == "__main__":
    main()
