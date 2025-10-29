#!/usr/bin/env python
import argparse
import os
from dotenv import load_dotenv

def cmd_health():
    from app import create_app
    app = create_app()
    with app.app_context():
        print("OK: app factory created; health:", {"status": "ok"})

def cmd_db_create_all():
    from app import create_app
    from app.db import db
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Created all tables (no migrations).")

def cmd_db_drop_all():
    from app import create_app
    from app.db import db
    app = create_app()
    with app.app_context():
        db.drop_all()
        print("Dropped all tables.")

def cmd_seed():
    import seed as seed_module
    seed_module.main()

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="SmartTutor backend manager")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("health")
    sub.add_parser("db_create_all")
    sub.add_parser("db_drop_all")
    sub.add_parser("seed")
    args = parser.parse_args()
    if args.cmd == "health":
        cmd_health()
    elif args.cmd == "db_create_all":
        cmd_db_create_all()
    elif args.cmd == "db_drop_all":
        cmd_db_drop_all()
    elif args.cmd == "seed":
        cmd_seed()
    else:
        parser.print_help()
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
