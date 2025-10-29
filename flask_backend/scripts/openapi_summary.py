#!/usr/bin/env python
"""
Fetch /openapi.json and print a compact summary:
- Total paths
- Tags list
"""
import json
import sys
import urllib.request

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    url = f"{base.rstrip('/')}/openapi.json"
    with urllib.request.urlopen(url, timeout=8) as resp:
        spec = json.loads(resp.read().decode("utf-8"))
    paths = spec.get("paths", {}) or {}
    tags = [t.get("name") for t in (spec.get("tags") or [])]
    print(f"Paths: {len(paths)}")
    print("Tags:", ", ".join(tags) if tags else "(none)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
