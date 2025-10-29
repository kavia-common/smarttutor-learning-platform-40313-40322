#!/usr/bin/env python
"""
Download OpenAPI JSON from the running service and save it to openapi.json.
Usage: python scripts/write_openapi_file.py [base_url] [output_path]
Defaults: base_url=http://localhost:8000, output_path=./openapi.json
"""
import json
import sys
import urllib.request
from pathlib import Path

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("openapi.json")
    url = f"{base.rstrip('/')}/openapi.json"
    with urllib.request.urlopen(url, timeout=8) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    # Basic validation keys
    if "openapi" not in data or "paths" not in data or "info" not in data:
        print("Invalid OpenAPI JSON: missing required keys")
        return 2
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Wrote {out_path.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
