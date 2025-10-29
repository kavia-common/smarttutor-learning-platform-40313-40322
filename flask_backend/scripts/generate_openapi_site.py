#!/usr/bin/env python
"""
Generate a simple static site for OpenAPI using Redoc:
- copies docs/openapi.html
- downloads /openapi.json to docs/openapi.json

Usage:
  python scripts/generate_openapi_site.py [base_url]
"""
import json
import sys
import urllib.request
from pathlib import Path

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    url = f"{base.rstrip('/')}/openapi.json"
    out_dir = Path("docs")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Copy template html
    src_html = Path("docs/openapi.html")
    if not src_html.exists():
        # Fallback: try from flask_backend/docs/openapi.html if running from repo root
        repo_html = Path(__file__).resolve().parent.parent / "docs" / "openapi.html"
        if repo_html.exists():
            src_html.write_text(repo_html.read_text(encoding="utf-8"), encoding="utf-8")
        else:
            # If neither exists, create a minimal placeholder
            src_html.write_text("<!doctype html><title>API Docs</title><p>Place openapi.html here.</p>", encoding="utf-8")
    # Fetch OpenAPI JSON
    with urllib.request.urlopen(url, timeout=8) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    (out_dir / "openapi.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Wrote {str((out_dir / 'openapi.json').resolve())}")
    print(f"Open docs/openapi.html in a browser; it will load /openapi.json by default.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
