#!/usr/bin/env python
import json
import sys
import urllib.parse
import urllib.request

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    course_id = sys.argv[2] if len(sys.argv) > 2 else None
    qs = f"?{urllib.parse.urlencode({'course_id': course_id})}" if course_id else ""
    url = f"{base.rstrip('/')}/api/whiteboard/sessions{qs}"
    with urllib.request.urlopen(url, timeout=8) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(data, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
