#!/usr/bin/env python
from app import create_app
from app.db import db

def main():
    app = create_app()
    with app.app_context():
        tables = list(db.Model.metadata.tables.keys())
        print("Tables:", ", ".join(sorted(tables)))

if __name__ == "__main__":
    main()
