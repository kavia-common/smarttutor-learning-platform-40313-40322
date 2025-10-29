# Contributing to SmartTutor

Repository layout:
- Frontend (React/Flutter hybrid scaffolding): smarttutor-learning-platform-40313-40322/react_frontend
- Backend (Flask): smarttutor-learning-platform-40313-40322/flask_backend

Quick start (backend):
1) cp flask_backend/.env.example flask_backend/.env
2) python -m venv .venv && source .venv/bin/activate
3) pip install -r flask_backend/requirements.txt
4) alembic upgrade head
5) python flask_backend/run_dev.py

Quick start (docker-compose):
1) cp flask_backend/.env.example flask_backend/.env
2) docker compose up --build -d
3) docker compose exec backend alembic upgrade head

Quick start (frontend React):
1) cd react_frontend
2) cp .env.example .env
3) npm install
4) npm run dev

CI notes:
- If Flutter analyzers are used, set working directory to smarttutor-learning-platform-40313-40322/react_frontend.
- Use scripts/check_backend_health.py to validate backend health in CI.

Code style (backend):
- Optional: pip install -r flask_backend/requirements-dev.txt
- black, isort, flake8 are available as dev tools.
