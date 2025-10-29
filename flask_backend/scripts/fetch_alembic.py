#!/usr/bin/env python
"""
Fetch Alembic current revision via CLI and print output.
"""
import subprocess
import sys

def main() -> int:
    try:
        out = subprocess.check_output(["alembic", "current"], stderr=subprocess.STDOUT, text=True)
        print(out.strip())
        return 0
    except subprocess.CalledProcessError as e:
        print(e.output)
        return e.returncode
    except FileNotFoundError:
        print("Alembic not found. Install dependencies and ensure it's on PATH.", file=sys.stderr)
        return 127

if __name__ == "__main__":
    raise SystemExit(main())
