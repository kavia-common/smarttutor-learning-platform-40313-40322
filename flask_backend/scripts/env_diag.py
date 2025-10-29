#!/usr/bin/env python
"""
Print key environment diagnostics for backend troubleshooting.
"""
import os

def main() -> int:
    print("PORT:", os.getenv("PORT", "<not set>"))
    print("DATABASE_URL:", "<set>" if os.getenv("DATABASE_URL") else "<not set>")
    print("JWT_SECRET:", "<set>" if os.getenv("JWT_SECRET") else "<not set>")
    print("ALLOWED_ORIGINS:", os.getenv("ALLOWED_ORIGINS", "<not set>"))
    print("LOG_LEVEL:", os.getenv("LOG_LEVEL", "<not set>"))
    print("PWD_PEPPER:", "<set>" if os.getenv("PWD_PEPPER") else "<not set>")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
