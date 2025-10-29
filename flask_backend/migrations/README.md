# Alembic Migrations

- Environment is configured in `migrations/env.py` to use Flask app metadata and `DATABASE_URL`.
- To create a new migration from model changes:
  alembic revision --autogenerate -m "message"

- To apply migrations:
  alembic upgrade head

Helpers:
- scripts/gen_migration.py – generate a migration with a message
- scripts/autogen_and_upgrade.py – generate and upgrade in one step
