#!/usr/bin/env python
"""
Print SQLAlchemy models and basic relationship info.
"""
from app import create_app
from app.db import db

def main() -> int:
    app = create_app()
    with app.app_context():
        for name, table in sorted(db.Model.metadata.tables.items()):
            print(f"- {name}")
        return 0

if __name__ == "__main__":
    raise SystemExit(main())
