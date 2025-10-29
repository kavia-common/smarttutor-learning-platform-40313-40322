#!/usr/bin/env python
"""
Create a .env from .env.example if missing. Useful for quick onboarding.
"""
from pathlib import Path

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    env = root / ".env"
    example = root / ".env.example"
    if env.exists():
        print(".env already exists. No action taken.")
        return 0
    if not example.exists():
        print("ERROR: .env.example not found")
        return 1
    env.write_text(example.read_text())
    print("Created .env from .env.example. Please update values as needed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
