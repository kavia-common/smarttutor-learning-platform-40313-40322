# SmartTutor – Monorepo

This workspace contains:
- React Frontend (Vite + TypeScript): smarttutor-learning-platform-40313-40322/react_frontend
- Flask Backend (PostgreSQL + SQLAlchemy + Alembic): smarttutor-learning-platform-40313-40322/flask_backend

Quick start

Frontend (React):
1) cd smarttutor-learning-platform-40313-40322/react_frontend
2) cp .env.example .env
3) npm install
4) npm run dev  # http://localhost:3000

Backend (Flask):
1) cd smarttutor-learning-platform-40313-40322/flask_backend
2) cp .env.example .env  # Update DATABASE_URL and JWT_SECRET
3) python -m venv .venv && . .venv/bin/activate
4) pip install -r requirements.txt
5) alembic upgrade head  # applies initial migration (migrations/versions/0001_initial.py)
6) python seed.py  # optional – adds sample users, course, and lessons
7) python wsgi.py  # http://localhost:8000/health

Docs:
- BACKEND_QUICK_START.md – backend setup
- INTEGRATION_CHECKLIST.md – end-to-end wiring
- CI_GUIDANCE.md – configure CI to use React app, not Flutter

Note:
Some Flutter scaffolding exists in react_frontend/, but the active web app is React. Configure CI to build the React app and test the Flask backend to avoid "Flutter project root" errors.
