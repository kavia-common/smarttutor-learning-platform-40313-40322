#!/usr/bin/env python
"""
Check database connectivity using SQLAlchemy from the Flask app context.
"""
import sys
from app import create_app
from app.db import db

def main() -> int:
    app = create_app()
    with app.app_context():
        try:
            # Execute a lightweight query
            db.session.execute(db.text("SELECT 1"))
            print("Database connectivity: OK")
            return 0
        except Exception as e:
            print("Database connectivity: FAILED")
            print(repr(e), file=sys.stderr)
            return 1

if __name__ == "__main__":
    raise SystemExit(main())
