#!/usr/bin/env python
"""
Fetch /openapi.json and write it to docs/openapi.json for publishing.
Usage: python scripts/publish_openapi.py [base_url]
"""
import json
import sys
import urllib.request
from pathlib import Path

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    url = f"{base.rstrip('/')}/openapi.json"
    with urllib.request.urlopen(url, timeout=8) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    out_dir = Path("docs")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "openapi.json"
    out_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Wrote {out_file.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
