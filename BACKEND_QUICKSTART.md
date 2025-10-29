# SmartTutor Backend Quickstart

1) Setup environment
   cd smarttutor-learning-platform-40313-40322/flask_backend
   cp .env.example .env
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   # Optional for tests:
   pip install -r requirements-dev.txt

2) Database migrations
   alembic upgrade head

3) Seed some data (optional)
   python seed.py
   # Or a full sample set:
   python scripts/seed_all_sample.py

4) Run backend
   python run_dev.py
   # Open http://localhost:8000/health and http://localhost:8000/openapi.json

5) Diagnostics and checks
   python scripts/run_all_diagnostics.py
   python scripts/check_core_endpoints.py

Compose alternative:
- See COMPOSE_README.md to run Postgres + backend with Docker Compose.
