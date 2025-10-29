#!/usr/bin/env python
"""
Print the expected Flutter project root for CI tooling.
"""
from pathlib import Path

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    flutter_root = root / "smarttutor-learning-platform-40313-40322" / "react_frontend"
    print(str(flutter_root))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
