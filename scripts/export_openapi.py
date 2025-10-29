#!/usr/bin/env python
"""
Fetch the backend /openapi.json and save it to the repository root as openapi.json.
Usage:
  python scripts/export_openapi.py [base_url]
"""
import json
import sys
import urllib.request
from pathlib import Path

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    url = f"{base.rstrip('/')}/openapi.json"
    with urllib.request.urlopen(url, timeout=8) as resp:
        spec = json.loads(resp.read().decode("utf-8"))
    out = Path(__file__).resolve().parent.parent / "openapi.json"
    out.write_text(json.dumps(spec, indent=2), encoding="utf-8")
    print(f"Wrote {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
