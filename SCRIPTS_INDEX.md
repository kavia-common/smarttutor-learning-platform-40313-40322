# Scripts Index (Root)

Frontend helpers:
- scripts/ci_run_in_react_frontend.sh — Run arbitrary commands in the React frontend CWD
- scripts/ci_decide_and_run_frontend_checks.sh — Decide between Flutter/React checks and run them
- scripts/ci_safe_flutter_analyze.sh — Safely attempt Flutter analyze (skips if non-applicable)
- scripts/print_react_root.py — Print the React project root
- scripts/print_flutter_root.py — Print the Flutter project root (if applicable)

Backend helpers:
- scripts/run_backend_dev.py — Start Flask backend in dev mode
- scripts/run_backend_gunicorn.py — Start Flask backend with Gunicorn
- scripts/check_backend_health.py — Hit /health and /openapi.json
- scripts/export_openapi.py — Save current /openapi.json to repo-root openapi.json
- scripts/compose_migrate_and_seed.sh — Run Alembic upgrade and seed in Docker Compose backend
- scripts/ensure_backend_env.py — Create backend .env from .env.example if missing
- flask_backend/scripts/ping_all_endpoints.py — Ping common endpoints and print statuses

Environment:
- scripts/validate_envs.py — Validate backend and frontend .env variables

General:
- scripts/print_workspace_tree.py — Print shallow workspace tree (navigation aid)
