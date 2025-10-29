#!/usr/bin/env python
"""
Print database schema (tables and columns) using SQLAlchemy inspector.
"""
from dotenv import load_dotenv

def main() -> int:
    load_dotenv()
    from app import create_app
    from app.db import db
    from sqlalchemy import inspect
    app = create_app()
    with app.app_context():
        engine = db.get_engine()
        insp = inspect(engine)
        for t in insp.get_table_names():
            print(f"Table: {t}")
            for c in insp.get_columns(t):
                print(f"  - {c['name']} ({c.get('type')}) nullable={c.get('nullable')} default={c.get('default')}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
