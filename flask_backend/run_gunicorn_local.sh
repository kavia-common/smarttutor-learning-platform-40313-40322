#!/usr/bin/env bash
# Local development helper to run Gunicorn
# Usage:
#   cd smarttutor-learning-platform-40313-40322/flask_backend
#   ./run_gunicorn_local.sh
set -euo pipefail
cd "$(dirname "$0")"
# Ensure .env exists for local dev
python scripts/bootstrap_env.py || true
# Apply migrations if DB configured (best effort)
if [ -n "${DATABASE_URL:-}" ]; then
  alembic upgrade head || echo "WARNING: alembic upgrade failed (continuing)"
fi
export LOG_LEVEL=${LOG_LEVEL:-INFO}
exec gunicorn -c gunicorn.conf.py wsgi:app
