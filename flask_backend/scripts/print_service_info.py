#!/usr/bin/env python
"""
Print basic service info and exit. Useful for CI/container probes.
"""
from app.constants import APP_NAME, APP_VERSION

def main() -> int:
    print(f"Service: {APP_NAME}")
    print(f"Version: {APP_VERSION}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
