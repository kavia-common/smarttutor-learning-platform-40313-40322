#!/usr/bin/env python
"""
List pending Alembic migrations from current to head.
"""
from alembic.config import Config
from alembic.script import ScriptDirectory
from alembic.runtime.migration import MigrationContext
from sqlalchemy import create_engine
import os

def main() -> int:
    cfg = Config("alembic.ini")
    script = ScriptDirectory.from_config(cfg)
    url = os.getenv("DATABASE_URL")
    if not url:
        print("DATABASE_URL not set.")
        return 1
    engine = create_engine(url)
    with engine.connect() as conn:
        context = MigrationContext.configure(conn)
        current = context.get_current_revision()
        head = script.get_current_head()
        print("Current revision:", current)
        print("Head revision:", head)
        if current == head:
            print("No pending migrations.")
            return 0
        revs = list(script.iterate_revisions(head, current))
        print("Pending migrations (newest first):")
        for r in revs:
            print(f"- {r.revision}: {r.doc or r.message}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
