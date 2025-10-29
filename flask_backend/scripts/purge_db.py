#!/usr/bin/env python
"""
Drop all tables and recreate them from models (bypassing migrations).
Use for local development only.
"""
from dotenv import load_dotenv

def main() -> int:
    load_dotenv()
    from app import create_app
    from app.db import db

    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Dropped and recreated all tables.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
