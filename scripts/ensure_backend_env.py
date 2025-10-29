#!/usr/bin/env python
"""
Ensure the backend .env file exists by copying from .env.example if missing.
"""
from pathlib import Path
import shutil
import sys

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    backend = root / "smarttutor-learning-platform-40313-40322" / "flask_backend"
    env_file = backend / ".env"
    example = backend / ".env.example"
    if env_file.exists():
        print("Backend .env already exists.")
        return 0
    if not example.exists():
        print("ERROR: .env.example not found at", example, file=sys.stderr)
        return 2
    shutil.copyfile(example, env_file)
    print(f"Created {env_file} from .env.example. Please update JWT_SECRET and DATABASE_URL.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
