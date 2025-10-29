#!/usr/bin/env python
import json
import time
import urllib.request

BASE = "http://localhost:8000"

def get(path: str):
    url = f"{BASE}{path}"
    with urllib.request.urlopen(url, timeout=5) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main():
    # Give the service a moment to start if run in CI
    for _ in range(5):
        try:
            print("health:", get("/health"))
            break
        except Exception:
            time.sleep(0.5)
    print("status:", get("/api/status"))
    print("version:", get("/api/version"))
    print("uptime:", get("/api/uptime"))
    print("memory:", get("/api/memory"))
    print("metrics:", get("/api/metrics"))
    print("proc:", get("/api/proc"))
    print("cpu:", get("/api/cpu"))

if __name__ == "__main__":
    main()
