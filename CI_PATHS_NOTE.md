CI Paths Note

This monorepo contains multiple scaffolds. Use these paths for CI:

Frontend (React Vite):
- working-directory: smarttutor-learning-platform-40313-40322/react_frontend
- steps:
  - cp .env.example .env
  - npm ci
  - npm run build

Backend (Flask):
- working-directory: smarttutor-learning-platform-40313-40322/flask_backend
- steps:
  - python -m venv .venv && . .venv/bin/activate
  - pip install -r requirements.txt
  - cp .env.example .env
  - alembic upgrade head || true  # optional for smoke
  - python scripts/smoke_health.py

Avoid invoking Flutter tooling in this pipeline unless you intend to build a separate Flutter app. The web frontend for SmartTutor is React (Vite) in the path above.
