#!/usr/bin/env python
"""
Run backend unit tests with pytest. If pytest is not installed, provide guidance.
"""
import subprocess
import sys

def main() -> int:
    try:
        return subprocess.call(["pytest", "-q"])
    except FileNotFoundError:
        print("pytest not found. Run: pip install -r requirements-dev.txt", file=sys.stderr)
        return 127

if __name__ == "__main__":
    raise SystemExit(main())
