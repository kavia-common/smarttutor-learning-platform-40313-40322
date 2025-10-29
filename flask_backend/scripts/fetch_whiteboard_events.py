#!/usr/bin/env python
import json
import sys
import urllib.request

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    session_id = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    url = f"{base.rstrip('/')}/api/whiteboard/sessions/{session_id}/events"
    with urllib.request.urlopen(url, timeout=8) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(data, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
