# Contributing to SmartTutor Flask Backend

- Create a virtualenv and install requirements: `pip install -r requirements.txt`
- Configure environment: copy `.env.example` to `.env` and set variables.
- Database migrations with Alembic:
  - `alembic revision --autogenerate -m "message"`
  - `alembic upgrade head`
- Run diagnostics: `python scripts/run_all_diagnostics.py`
- Start dev server: `python run_dev.py`

Coding style:
- Use app factory pattern (create_app).
- Add docstrings for public interfaces and route functions.
- Avoid hardcoding configuration; read from environment.
- Keep migrations in sync with models (autogenerate and review).
