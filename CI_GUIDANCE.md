CI Guidance – SmartTutor

Context:
The repository includes scaffolded Flutter files, but the active web frontend is React (Vite + TypeScript) located at:
  smarttutor-learning-platform-40313-40322/react_frontend

To avoid CI failures like "Could not determine project root directory for Flutter project", configure CI to:
- Build React web frontend:
    - working-directory: smarttutor-learning-platform-40313-40322/react_frontend
    - commands:
        - cp .env.example .env
        - npm ci
        - npm run build
- Test Flask backend:
    - working-directory: smarttutor-learning-platform-40313-40322/flask_backend
    - commands:
        - python -m venv .venv
        - . .venv/bin/activate
        - pip install -r requirements.txt
        - cp .env.example .env
        - alembic upgrade head
        - python -m pytest -q  # if tests are added
        - python wsgi.py  # or gunicorn app:wsgi if used in deploy

Environment variables to set in CI:
- For backend:
  - DATABASE_URL (PostgreSQL preferred; can use service container)
  - JWT_SECRET
  - LOG_LEVEL=INFO
- For frontend:
  - VITE_API_BASE_URL (e.g., http://localhost:8000/api)

Notes:
- Do not run Flutter analyzers/builds unless you specifically target the Flutter app. The current deliverable is the React web frontend.
- Backend listens on PORT 8000 by default and exposes /health and /openapi.json for readiness checks.
