#!/usr/bin/env python
"""
Fetch /openapi.json from a running backend and write it to ./openapi_dump.json.
Usage:
  python scripts/dump_openapi.py [base_url]
Default base_url: http://localhost:8000
"""
import json
import sys
import urllib.request
from pathlib import Path

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    url = f"{base.rstrip('/')}/openapi.json"
    with urllib.request.urlopen(url, timeout=5) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    out = Path(__file__).resolve().parent.parent / "openapi_dump.json"
    out.write_text(json.dumps(data, indent=2))
    print(f"Wrote {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
