#!/usr/bin/env python
"""
Call /api/dev/enroll with a given user_id and course_id.
Usage: python scripts/dev_enroll.py [base_url] user_id course_id
Defaults: base_url=http://localhost:8000
"""
import json
import sys
import urllib.request

def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python scripts/dev_enroll.py [base_url] user_id course_id")
        return 2
    if len(sys.argv) == 3:
        base = "http://localhost:8000"
        user_id = int(sys.argv[1])
        course_id = int(sys.argv[2])
    else:
        base = sys.argv[1]
        user_id = int(sys.argv[2])
        course_id = int(sys.argv[3])

    url = f"{base.rstrip('/')}/api/dev/enroll"
    body = json.dumps({"user_id": user_id, "course_id": course_id}).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=8) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(data, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
