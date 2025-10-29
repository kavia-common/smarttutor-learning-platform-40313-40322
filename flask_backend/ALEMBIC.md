Alembic usage

- Ensure .env is present with DATABASE_URL and JWT_SECRET.
- Create venv and install dependencies:
  python -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt

- Apply migrations:
  alembic upgrade head

- Create a new migration (autogenerate):
  alembic revision --autogenerate -m "your message"

- Downgrade (example):
  alembic downgrade -1
