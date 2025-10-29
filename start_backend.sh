#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/smarttutor-learning-platform-40313-40322/flask_backend"
python scripts/bootstrap_env.py || true
export PORT="${PORT:-8000}"
python wsgi.py
