#!/usr/bin/env python
"""
Create or update a developer superuser for quick manual testing.
"""
import os
from dotenv import load_dotenv

def main() -> int:
    load_dotenv()
    os.environ.setdefault("DATABASE_URL", "sqlite:///smarttutor.db")
    os.environ.setdefault("JWT_SECRET", "dev_only_secret_change_me")
    from app import create_app
    from app.db import db
    from app.models import User
    from app.security import hash_password

    email = os.getenv("DEV_ADMIN_EMAIL", "admin@example.com")
    password = os.getenv("DEV_ADMIN_PASSWORD", "admin123")
    name = os.getenv("DEV_ADMIN_NAME", "Admin")

    app = create_app()
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        salt, pw_hash = hash_password(password)
        if user:
            user.name = name
            user.password_hash = f"{salt}:{pw_hash}"
            user.role = "admin"
            print(f"Updated existing admin: {email}")
        else:
            user = User(email=email, name=name, password_hash=f"{salt}:{pw_hash}", role="admin")
            db.session.add(user)
            print(f"Created new admin: {email}")
        db.session.commit()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
