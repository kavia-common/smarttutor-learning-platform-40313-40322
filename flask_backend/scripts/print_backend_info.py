#!/usr/bin/env python
"""
Print backend environment/config info to help verify local setup.
"""
import os
from dotenv import load_dotenv

def main() -> int:
    load_dotenv()
    api_base = "http://localhost:%s/api" % (os.getenv("PORT", "8000"))
    ws_base = "ws://localhost:%s/ws" % (os.getenv("PORT", "8000"))
    print(f"DATABASE_URL={os.getenv('DATABASE_URL', '')}")
    print(f"JWT_SECRET={'(set)' if os.getenv('JWT_SECRET') else '(missing)'}")
    print(f"ALLOWED_ORIGINS={os.getenv('ALLOWED_ORIGINS', '') or '(dev allow-all)'}")
    print(f"API_BASE={api_base}")
    print(f"WS_BASE={ws_base}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
