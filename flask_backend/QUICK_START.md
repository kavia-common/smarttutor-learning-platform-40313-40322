# Quick Start (Flask Backend)

1) Copy env and install
   cp .env.example .env
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt

2) Database and migrations
   python scripts/ensure_initial_migration.py
   alembic upgrade head

3) Seed data
   python seed.py
   # or export/import
   python scripts/seed_export.py
   python scripts/seed_import.py seed_export.json

4) Run
   make run
   # Open http://localhost:8000/health and /openapi.json

Diagnostics:
- make openapi
- python scripts/run_all_diagnostics.py
- python scripts/smoke_all_in_one.py
