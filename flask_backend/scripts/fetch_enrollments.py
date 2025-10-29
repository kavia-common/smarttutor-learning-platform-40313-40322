#!/usr/bin/env python
"""
Fetch /api/users/{id}/enrollments and pretty-print it.
"""
import json
import sys
import urllib.request

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    user_id = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    url = f"{base.rstrip('/')}/api/users/{user_id}/enrollments"
    with urllib.request.urlopen(url, timeout=6) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(data, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
