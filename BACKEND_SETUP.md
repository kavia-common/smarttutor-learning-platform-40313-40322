SmartTutor Flask Backend (flask_backend)

Location:
- smarttutor-learning-platform-40313-40322/flask_backend

Quick start:
1) cd smarttutor-learning-platform-40313-40322/flask_backend
2) cp .env.example .env and set DATABASE_URL (e.g., postgresql+psycopg://user:pass@localhost:5432/smarttutor) and JWT_SECRET
3) python -m venv .venv && source .venv/bin/activate
4) pip install -r requirements.txt
5) Initialize DB: python init_db.py
6) Optional: seed sample data: python seed.py
7) Run server: python run_dev.py
   - App will serve on http://localhost:8000
   - Health: http://localhost:8000/health
   - API root: http://localhost:8000/api/
   - OpenAPI: http://localhost:8000/openapi.json
   - WebSocket docs (stub): http://localhost:8000/docs/ws

Frontend wiring:
- In react_frontend/.env (.env.example provided), set:
  VITE_API_BASE_URL=http://localhost:8000/api
  VITE_WS_BASE_URL=ws://localhost:8000/ws

Notes:
- Backend prefers PostgreSQL. Ensure a running Postgres and proper DATABASE_URL.
- Migrations via Alembic (manage.py wraps alembic with .env loading).
- CORS is enabled for /api/* in development (allow-all). Restrict in production.
