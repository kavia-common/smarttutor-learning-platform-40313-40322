#!/usr/bin/env python
import subprocess
import sys

def main() -> int:
    try:
        out = subprocess.check_output(["alembic", "history"], stderr=subprocess.STDOUT, text=True)
        print(out)
        return 0
    except subprocess.CalledProcessError as e:
        print(e.output)
        return e.returncode

if __name__ == "__main__":
    raise SystemExit(main())
