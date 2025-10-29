#!/usr/bin/env python
"""
Print the React project root for CI/tooling and exit non-zero if not found.
"""
from pathlib import Path
import sys

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    react_root = root / "smarttutor-learning-platform-40313-40322" / "react_frontend"
    print("Expected React root:", react_root)
    if not react_root.exists():
        print("ERROR: React project root path does not exist.", file=sys.stderr)
        return 1
    pkg = react_root / "package.json"
    if not pkg.exists():
        print("ERROR: package.json not found in React root.", file=sys.stderr)
        return 2
    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
