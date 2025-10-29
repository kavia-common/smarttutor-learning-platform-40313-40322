#!/usr/bin/env python
"""
Exit non-zero if Alembic current head cannot be determined.
Useful in CI to ensure migrations wiring is healthy.
"""
from alembic.config import Config
from alembic.script import ScriptDirectory

def main() -> int:
    try:
        cfg = Config("alembic.ini")
        script = ScriptDirectory.from_config(cfg)
        head = script.get_current_head()
        print("Alembic head:", head)
        return 0
    except Exception as e:
        print("ERROR: Unable to get Alembic head:", e)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
