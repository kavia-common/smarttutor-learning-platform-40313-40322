#!/usr/bin/env python
"""
Generate an Alembic migration using current SQLAlchemy models.
Usage:
  python scripts/gen_migration.py "your message"
"""
import sys
from dotenv import load_dotenv
from alembic.config import Config
from alembic import command

def main() -> int:
    load_dotenv()
    msg = "auto"
    if len(sys.argv) > 1:
        msg = sys.argv[1]
    cfg = Config("alembic.ini")
    command.revision(cfg, autogenerate=True, message=msg)
    print(f"Generated migration with message: {msg}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
