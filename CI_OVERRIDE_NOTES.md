CI Override Notes

The repository contains Flutter scaffolding but the active web frontend is React (Vite). To avoid CI failures like:
  "Could not determine project root directory for Flutter project"

Ensure CI pipelines:
- Do NOT run flutter analyze, flutter pub get, or flutter build unless a dedicated Flutter job is desired.
- DO run:
  - Frontend (React):
      working-directory: smarttutor-learning-platform-40313-40322/react_frontend
      steps:
        - cp .env.example .env
        - npm ci
        - npm run build
  - Backend (Flask):
      working-directory: smarttutor-learning-platform-40313-40322/flask_backend
      steps:
        - python -m venv .venv && . .venv/bin/activate
        - pip install -r requirements.txt
        - cp .env.example .env
        - alembic upgrade head || true  # optional in CI smoke
        - python scripts/smoke_health.py

Tip:
- Use run_backend_smoke.py or print_backend_routes.py from repo root to quickly validate backend wiring during CI.
