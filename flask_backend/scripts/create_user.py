#!/usr/bin/env python
"""
Create a development user quickly.
Usage: python scripts/create_user.py email name [role]
"""
import sys
from app import create_app
from app.db import db
from app.models import User

def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python scripts/create_user.py email name [role]")
        return 2
    email = sys.argv[1]
    name = sys.argv[2]
    role = sys.argv[3] if len(sys.argv) > 3 else "student"
    app = create_app()
    with app.app_context():
        if db.session.query(User).filter_by(email=email).first():
            print("User already exists")
            return 0
        u = User(email=email, name=name, role=role, password_hash="dev")
        db.session.add(u)
        db.session.commit()
        print("Created user:", u.id, u.email)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
