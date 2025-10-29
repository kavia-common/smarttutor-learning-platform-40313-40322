#!/usr/bin/env python
"""
Generate a salted password hash for development seeding.
This uses werkzeug.security for simplicity.
"""
import sys
try:
    from werkzeug.security import generate_password_hash
except Exception as e:
    print("Missing dependency: Werkzeug (install via Flask).", file=sys.stderr)
    raise

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/hash_password.py <password>", file=sys.stderr)
        return 2
    pwd = sys.argv[1]
    hashed = generate_password_hash(pwd)
    print(hashed)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
