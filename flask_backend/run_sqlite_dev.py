#!/usr/bin/env python
"""
Run backend quickly using a local SQLite file if DATABASE_URL is not set.
This is for development smoke checks only; production should use PostgreSQL.
"""
import os
from wsgi import app

def main():
    os.environ.setdefault("DATABASE_URL", "sqlite:///smarttutor.db")
    os.environ.setdefault("JWT_SECRET", "dev_only_secret_change_me")
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=True)

if __name__ == "__main__":
    main()
