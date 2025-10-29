#!/usr/bin/env python
"""
Create all SQLAlchemy tables using db.create_all().

Intended for local development or sqlite test environments only.
For production databases, use Alembic migrations instead.
"""
from dotenv import load_dotenv

def main() -> int:
    load_dotenv()
    from app import create_app
    from app.db import db
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Created all tables via SQLAlchemy metadata.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
