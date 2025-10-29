#!/usr/bin/env python
"""
Start the backend (if not already running) and run basic smoke tests.
This script is intended for local quick checks; it does not daemonize.
"""
import os
import subprocess
import sys
import time
import urllib.request

BASE = "http://localhost:8000"

def is_up(url: str) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=3) as _:
            return True
    except Exception:
        return False

def main() -> int:
    base = os.getenv("BASE_URL", BASE)
    # If service isn't up, attempt to run wsgi.py
    started = False
    if not is_up(f"{base.rstrip('/')}/health"):
        env = os.environ.copy()
        env.setdefault("PORT", "8000")
        proc = subprocess.Popen([sys.executable, "wsgi.py"], env=env)
        started = True
        # Wait a few seconds for server to start
        for _ in range(20):
            if is_up(f"{base.rstrip('/')}/health"):
                break
            time.sleep(0.3)
    # Run basic smoke
    rc = subprocess.call([sys.executable, "scripts/smoke_basic.py", base])
    # We don't terminate the process if we started it, since wsgi.py exits on Ctrl+C.
    if started:
        try:
            proc.terminate()
        except Exception:
            pass
    return rc

if __name__ == "__main__":
    raise SystemExit(main())
