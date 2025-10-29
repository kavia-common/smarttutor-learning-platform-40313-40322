#!/usr/bin/env bash
set -euo pipefail
if [ -f ".env" ]; then
  # shellcheck disable=SC2046
  export $(grep -v '^\s*#' .env | xargs) || true
fi
export PORT="${PORT:-8000}"
echo "Starting SmartTutor backend on http://localhost:${PORT}"
python wsgi.py
