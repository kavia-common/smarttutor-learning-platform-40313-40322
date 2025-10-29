#!/usr/bin/env python
"""
Show pending Alembic autogenerate diffs without creating a file.

This runs 'alembic revision --autogenerate' in a temp directory and prints the diff,
then removes the temporary revision file to avoid polluting migrations.
"""
import subprocess
import tempfile
import shutil
from pathlib import Path

def main() -> int:
    tmpdir = tempfile.mkdtemp(prefix="alembic_diff_")
    try:
        # Create a temporary revision file
        proc = subprocess.run(
            ["alembic", "revision", "--autogenerate", "-m", "temp_show_diff"],
            capture_output=True, text=True
        )
        if proc.returncode != 0:
            print(proc.stdout)
            print(proc.stderr)
            return proc.returncode

        # Find most recent file under migrations/versions
        versions = Path("migrations/versions")
        rev_files = sorted(versions.glob("*.py"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not rev_files:
            print("No revision file generated; nothing to show.")
            return 0
        latest = rev_files[0]
        print(f"--- BEGIN DIFF ({latest.name}) ---")
        print(latest.read_text(encoding="utf-8"))
        print(f"--- END DIFF ({latest.name}) ---")

        # Remove the temporary revision file
        latest.unlink(missing_ok=True)
        return 0
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

if __name__ == "__main__":
    raise SystemExit(main())
