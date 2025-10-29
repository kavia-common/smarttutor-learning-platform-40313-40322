# Backend Environment

Required variables (in .env under flask_backend):
- DATABASE_URL: SQLAlchemy URL to PostgreSQL (SQLAlchemy 2.x)
  Example: postgresql+psycopg://postgres:postgres@localhost:5432/smarttutor
- JWT_SECRET: Random long string for signing JWTs
- PORT: Defaults to 8000 (optional)

Notes:
- Prefer psycopg 3 driver (`postgresql+psycopg`).
- Do not hardcode secrets; always use environment variables.

Docker Compose:
- The root-level docker-compose.yml starts a Postgres service and the backend.
- The backend’s DATABASE_URL is overridden to point to the compose `db` service.

Common commands:
- alembic upgrade head
- python seed.py
- python run_dev.py
