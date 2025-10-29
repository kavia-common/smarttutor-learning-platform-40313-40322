Alembic – Quick Reference

Common commands:
- Upgrade to latest:
  alembic upgrade head

- Downgrade one step:
  alembic downgrade -1

- Show current head(s):
  alembic heads

- Autogenerate a new migration from models:
  alembic revision --autogenerate -m "your message"
  # or: python scripts/gen_migration.py "your message"

Troubleshooting:
- Ensure DATABASE_URL is set in .env
- Ensure models are imported in app/__init__.py so Alembic sees metadata
- If autogeneration misses changes, verify relationships and constraints are declared
