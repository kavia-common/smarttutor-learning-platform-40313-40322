# Database Guide

Connection string:
- PostgreSQL (preferred):
  - postgresql+psycopg://USER:PASSWORD@HOST:PORT/DBNAME
  - Example: postgresql+psycopg://postgres:password@localhost:5432/smarttutor
- SQLite (for tests/dev only):
  - sqlite+pysqlite:///absolute/path/to/file.db
  - sqlite+pysqlite:///:memory: (tests)

Environment:
- DATABASE_URL and JWT_SECRET are required to start the app.
- APP_VERSION is optional and appears in headers (X-App-Version).

Alembic:
- Create migration: alembic revision --autogenerate -m "message"
- Apply migrations: alembic upgrade head
- Downgrade one step: alembic downgrade -1
- Ensure initial migration (if missing): python scripts/ensure_initial_migration.py

One-shot setup:
- python scripts/db_setup.py --seed

Troubleshooting:
- If migrations fail, ensure DATABASE_URL points to a reachable DB.
- For Postgres in Docker, ensure the container port is published and reachable from host.
