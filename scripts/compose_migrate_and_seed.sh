#!/usr/bin/env bash
set -euo pipefail
# Run Alembic migrations and seed data inside the backend container.
echo "Running alembic upgrade head..."
docker compose exec backend alembic upgrade head
echo "Seeding sample data..."
docker compose exec backend python seed.py
echo "Done."
