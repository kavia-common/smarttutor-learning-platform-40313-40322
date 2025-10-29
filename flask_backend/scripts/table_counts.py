#!/usr/bin/env python
from app import create_app
from app.db import db

def count(table_name: str) -> int:
    return db.session.execute(db.text(f"SELECT COUNT(*) FROM {table_name}")).scalar_one()

def main():
    app = create_app()
    with app.app_context():
        names = sorted(db.Model.metadata.tables.keys())
        for name in names:
            try:
                c = count(name)
            except Exception as e:
                print(f"{name}: error: {e}")
            else:
                print(f"{name}: {c}")

if __name__ == "__main__":
    main()
