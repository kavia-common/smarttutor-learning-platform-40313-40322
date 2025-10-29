#!/usr/bin/env python
"""
Start the SmartTutor Flask backend for local development.

Usage:
  python scripts/dev_server.py
Environment:
  - Reads .env if present (DATABASE_URL, JWT_SECRET, PORT, APP_VERSION)
"""
import os
from dotenv import load_dotenv
from wsgi import get_app

def main() -> int:
    load_dotenv()
    app = get_app()
    port = int(os.getenv("PORT", "8000"))
    print(f"Starting SmartTutor backend on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
