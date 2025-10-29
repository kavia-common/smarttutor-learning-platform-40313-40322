#!/usr/bin/env python
"""
Print Flask backend routes from repo root to assist CI troubleshooting.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
BACKEND = ROOT / "smarttutor-learning-platform-40313-40322" / "flask_backend"

def main() -> int:
    if not BACKEND.exists():
        print("Backend directory not found:", BACKEND, file=sys.stderr)
        return 1
    sys.path.insert(0, str(BACKEND))
    from app import create_app
    app = create_app()
    with app.app_context():
        rules = sorted(app.url_map.iter_rules(), key=lambda r: r.rule)
        for r in rules:
            if r.endpoint == "static":
                continue
            methods = ",".join(sorted(m for m in r.methods if m not in ("HEAD", "OPTIONS")))
            print(f"{methods:<12} {r.rule:<40} {r.endpoint}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
