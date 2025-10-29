Troubleshooting – Flask Backend

Common issues:

1) DATABASE_URL or JWT_SECRET missing
- Symptom: RuntimeError raised on startup
- Fix: Copy .env.example to .env and set both values.

2) Postgres not reachable
- Symptom: Connection refused or timeout during migration or readiness check
- Fix: Start Postgres (docker compose up -d) and verify credentials/host in DATABASE_URL.

3) Alembic migration mismatch
- Symptom: Model changes not reflected in DB
- Fix:
  - make gen msg="your message"  # or python scripts/gen_migration.py "your message"
  - make upgrade

4) CORS blocked from React app
- Symptom: Browser CORS error on API calls
- Fix: Set ALLOWED_ORIGINS in .env (comma-separated), restart backend.

5) CI fails with Flutter project root error
- Symptom: "Could not determine project root directory for Flutter project"
- Fix: Configure CI to build React app at smarttutor-learning-platform-40313-40322/react_frontend.
  See CI_GUIDANCE.md for details.

6) Gunicorn in Docker doesn't apply migrations
- Symptom: Tables missing in container
- Fix: Ensure DATABASE_URL is set; container runs `alembic upgrade head` before starting.
  If it fails, run migration manually and check logs.

Diagnostics:
- /health – quick health check
- /api/diag/alembic – Alembic head and table list
- /api/diag/routes – list registered routes
- Scripts:
  - scripts/readiness_check.py
  - scripts/print_schema.py
  - scripts/export_seed_data.py
