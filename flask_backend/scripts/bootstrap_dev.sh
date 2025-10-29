#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$(cd "${HERE}/.." && pwd)"

cd "${BACKEND_DIR}"

if [[ ! -f ".env" ]]; then
  echo "ERROR: .env not found. Copy .env.example to .env and update values." >&2
  exit 2
fi

if [[ ! -d ".venv" ]]; then
  echo "Creating virtual environment..."
  python -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

echo "Installing dependencies..."
pip install -U pip
pip install -r requirements.txt

echo "Running migrations..."
alembic upgrade head

echo "Seeding data (optional step; will continue on failure)..."
python seed.py || true

echo "Starting development server on http://localhost:${PORT:-8000}"
python run_dev.py
