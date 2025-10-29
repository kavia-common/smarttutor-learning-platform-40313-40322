#!/usr/bin/env python
"""
Dump all Flask routes with methods and rules.
"""
from app import create_app

def main() -> int:
    app = create_app()
    with app.app_context():
        for rule in sorted(app.url_map.iter_rules(), key=lambda r: r.rule):
            methods = ",".join(sorted(m for m in rule.methods if m not in {"HEAD", "OPTIONS"}))
            print(f"{rule.rule:40s}  [{methods}]  -> {rule.endpoint}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
