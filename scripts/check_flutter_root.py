#!/usr/bin/env python
"""
Check and print the Flutter project root used by CI and analyzers.
Fails with non-zero exit code if the directory does not exist.
"""
from pathlib import Path
import sys

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    flutter_root = root / "smarttutor-learning-platform-40313-40322" / "react_frontend"
    print("Expected Flutter root:", flutter_root)
    if not flutter_root.exists():
        print("ERROR: Flutter project root path does not exist.", file=sys.stderr)
        return 1
    if not (flutter_root / "pubspec.yaml").exists():
        print("WARNING: pubspec.yaml not found under the expected Flutter root; hybrid template present.", file=sys.stderr)
    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
