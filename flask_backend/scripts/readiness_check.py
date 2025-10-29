#!/usr/bin/env python
"""
Backend readiness check:
- Ensures env vars
- Tests DB connection
- Verifies alembic can load and show head
- Calls /health
"""
import os
import sys
import urllib.request
from dotenv import load_dotenv

def main() -> int:
    load_dotenv()
    db_url = os.getenv("DATABASE_URL")
    jwt = os.getenv("JWT_SECRET")
    if not db_url or not jwt:
        print("ERROR: Missing DATABASE_URL or JWT_SECRET")
        return 1

    try:
        from alembic.config import Config
        from alembic.script import ScriptDirectory
        cfg = Config("alembic.ini")
        script = ScriptDirectory.from_config(cfg)
        head = script.get_current_head()
        print(f"Alembic head: {head}")
    except Exception as e:
        print(f"WARNING: Alembic head unavailable: {e}")

    try:
        from app import create_app
        from app.db import db
        app = create_app()
        with app.app_context():
            engine = db.get_engine()
            with engine.connect() as conn:
                conn.execute(db.text("SELECT 1"))
        print("DB connection: OK")
    except Exception as e:
        print(f"ERROR: DB connection failed: {e}")
        return 2

    url = f"http://localhost:{os.getenv('PORT', '8000')}/health"
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            if resp.status == 200:
                print("Health endpoint: OK")
            else:
                print(f"WARNING: Health endpoint status {resp.status}")
    except Exception as e:
        print(f"WARNING: Health endpoint not reachable: {e}")

    print("Readiness check completed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
