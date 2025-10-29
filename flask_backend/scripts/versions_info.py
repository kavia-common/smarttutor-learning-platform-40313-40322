#!/usr/bin/env python
"""
Print Python and key package versions to assist with diagnostics.
"""
import sys
import platform

def main() -> int:
    print("Python:", sys.version.replace("\n", " "))
    print("Platform:", platform.platform())
    try:
        import flask
        print("Flask:", flask.__version__)
    except Exception:
        print("Flask: not installed")
    try:
        import sqlalchemy
        print("SQLAlchemy:", sqlalchemy.__version__)
    except Exception:
        print("SQLAlchemy: not installed")
    try:
        import alembic
        print("Alembic:", alembic.__version__)
    except Exception:
        print("Alembic: not installed")
    try:
        import psycopg
        print("psycopg:", psycopg.__version__)
    except Exception:
        print("psycopg: not installed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
