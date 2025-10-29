#!/usr/bin/env python
"""
Start the Flask app briefly and check /health.
Intended for CI smoke verification when a long-running service isn't desired.
"""
import os
import threading
import time
import urllib.request

def run_server():
    os.environ.setdefault("PORT", "8000")
    from wsgi import app
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "8000")), debug=False, use_reloader=False)

def main() -> int:
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    time.sleep(1.5)  # give server time to start
    url = f"http://127.0.0.1:{os.getenv('PORT', '8000')}/health"
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            print("Health:", resp.status, resp.read().decode("utf-8"))
            return 0 if resp.status == 200 else 2
    except Exception as e:
        print("Smoke health failed:", e)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
