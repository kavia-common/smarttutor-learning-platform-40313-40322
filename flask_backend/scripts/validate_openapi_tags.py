#!/usr/bin/env python
"""
Validate that each path+method in /openapi.json has at least one tag for better documentation grouping.
"""
import json
import sys
import urllib.request

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    url = f"{base.rstrip('/')}/openapi.json"
    with urllib.request.urlopen(url, timeout=8) as resp:
        spec = json.loads(resp.read().decode("utf-8"))

    paths = spec.get("paths", {})
    missing = []
    for p, methods in paths.items():
        for m, details in (methods or {}).items():
            # OpenAPI keys are lower-case methods typically
            if not isinstance(details, dict):
                continue
            tags = details.get("tags")
            if not tags:
                missing.append((p, m))
    if missing:
        print("Entries without tags:")
        for p, m in missing[:20]:
            print(f"  {m.upper():6s} {p}")
        print(f"Total missing tags: {len(missing)}")
        return 1
    print("All path operations have tags.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
