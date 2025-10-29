Backend Developer Checklist

Local setup:
- [ ] Python 3.11 installed
- [ ] Create virtualenv: python -m venv .venv && . .venv/bin/activate
- [ ] Copy .env.example to .env and set DATABASE_URL + JWT_SECRET
- [ ] pip install -r requirements.txt
- [ ] Alembic upgrade: alembic upgrade head
- [ ] (Optional) Seed data: python seed.py or scripts/generate_dummy_data.py

Run:
- [ ] python wsgi.py  # http://localhost:8000/health
- [ ] curl http://localhost:8000/api/status
- [ ] curl http://localhost:8000/openapi.json

Diagnostics:
- scripts/env_diag.py             # print env info
- scripts/check_alembic_head.py   # verify alembic head
- scripts/verify_models.py        # ensure metadata/tables are visible
- scripts/table_counts.py         # table row counts
- scripts/print_config.py         # print Flask config

Testing:
- ./run_tests.sh
- or: make test

Docker:
- docker compose up -d db
- docker build -t smarttutor-backend .
- docker run -p 8000:8000 -e DATABASE_URL=... -e JWT_SECRET=... smarttutor-backend:latest

CI notes:
- Use SQLite for unit tests (DATABASE_URL=sqlite:///:memory:)
- Avoid Flutter analyzers; frontend is React at react_frontend/.
