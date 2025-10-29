#!/usr/bin/env python
"""
Print a combined summary of environment variables and service info.
"""
import os
from app import create_app

def main() -> int:
    app = create_app()
    with app.app_context():
        print("DATABASE_URL present:", bool(os.getenv("DATABASE_URL")))
        print("JWT_SECRET present:", bool(os.getenv("JWT_SECRET")))
        print("APP_VERSION:", os.getenv("APP_VERSION", "unset"))
        print("Registered routes:", len(list(app.url_map.iter_rules())))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
