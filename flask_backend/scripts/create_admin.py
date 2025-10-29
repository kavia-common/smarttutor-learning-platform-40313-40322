#!/usr/bin/env python
"""
Create an admin user for local development.

Usage:
  python scripts/create_admin.py --email admin@example.com --name "Admin" --password hash_or_placeholder
Note: This stores a provided password hash directly. Replace with a real hasher when auth is implemented.
"""
import argparse
from dotenv import load_dotenv
from app import create_app
from app.db import db
from app.models import User

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--email", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--password", required=True, help="Password hash or placeholder")
    args = parser.parse_args()

    load_dotenv()
    app = create_app()
    with app.app_context():
        existing = User.query.filter_by(email=args.email).first()
        if existing:
            print(f"User with email {args.email} already exists (id={existing.id}).")
            return 0
        user = User(email=args.email, name=args.name, password_hash=args.password, role="admin")
        db.session.add(user)
        db.session.commit()
        print(f"Created admin user with id={user.id}, email={user.email}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
