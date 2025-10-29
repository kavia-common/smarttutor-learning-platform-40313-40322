SmartTutor Flask Backend – Quick Start

1) Start Postgres locally (optional but recommended):
   cd smarttutor-learning-platform-40313-40322/flask_backend
   docker compose up -d

2) Setup Python env and install deps:
   make venv
   make install
   make env

3) Apply migrations and seed:
   make upgrade
   make seed

4) Run backend:
   make run
   # http://localhost:8000/health
   # http://localhost:8000/api/version
   # http://localhost:8000/openapi.json

5) Frontend (React Vite):
   cd smarttutor-learning-platform-40313-40322/react_frontend
   cp .env.example .env
   npm install
   npm run dev
   # http://localhost:3000

Notes:
- If CI complains about Flutter project root, ensure pipeline points to react_frontend for web build and flask_backend for backend tests.
- Configure DATABASE_URL (PostgreSQL) and JWT_SECRET in flask_backend/.env before running in a non-dev environment.
