# SmartTutor Integration Guide

Backend + Postgres via Docker Compose
1) cp smarttutor-learning-platform-40313-40322/flask_backend/.env.example smarttutor-learning-platform-40313-40322/flask_backend/.env
   - Set JWT_SECRET to a long random value
2) From repo root:
   docker compose up --build -d
3) Apply migrations:
   docker compose exec backend alembic upgrade head
4) Seed data (optional):
   docker compose exec backend python seed.py
5) Verify:
   curl http://localhost:8000/health
   curl http://localhost:8000/openapi.json

Frontend linkage
- In react_frontend, set:
  VITE_API_BASE_URL=http://localhost:8000
  VITE_WS_BASE_URL=ws://localhost:8000

Local development (without Docker)
- cd smarttutor-learning-platform-40313-40322/flask_backend
- python -m venv .venv && source .venv/bin/activate
- pip install -r requirements.txt
- cp .env.example .env
- alembic upgrade head
- python run_dev.py
