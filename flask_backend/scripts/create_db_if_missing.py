#!/usr/bin/env python
"""
Create the target Postgres database if it does not exist (development aid).
Uses the DATABASE_URL env var. Requires psycopg to be installed.
"""
import os
import sys
from urllib.parse import urlparse
import psycopg

def main() -> int:
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("DATABASE_URL not set.", file=sys.stderr)
        return 2

    parsed = urlparse(db_url)
    if parsed.scheme.split("+", 1)[0] != "postgresql":
        print("This helper only supports PostgreSQL URLs.", file=sys.stderr)
        return 3

    target_db = parsed.path.lstrip("/") or "postgres"
    admin_db_url = db_url.rsplit("/", 1)[0] + "/postgres"

    try:
        with psycopg.connect(admin_db_url, autocommit=True) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (target_db,))
                exists = cur.fetchone() is not None
                if exists:
                    print(f"Database '{target_db}' already exists.")
                    return 0
                cur.execute(f'CREATE DATABASE "{target_db}";')
                print(f"Created database '{target_db}'.")
                return 0
    except Exception as e:
        print("Error creating database:", e, file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
