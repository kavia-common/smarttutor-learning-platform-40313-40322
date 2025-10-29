#!/usr/bin/env python
"""
Print a shallow workspace tree to help developers and CI locate key files.
"""
from pathlib import Path

def print_tree(root: Path, depth: int = 2, prefix: str = ""):
    if depth < 0:
        return
    try:
        entries = sorted([p for p in root.iterdir()], key=lambda x: (not x.is_dir(), x.name.lower()))
    except Exception:
        return
    for p in entries:
        print(f"{prefix}{p.name}{'/' if p.is_dir() else ''}")
        if p.is_dir() and depth > 0:
            print_tree(p, depth - 1, prefix + "  ")

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    print("Workspace root:", root)
    print_tree(root, depth=2)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
