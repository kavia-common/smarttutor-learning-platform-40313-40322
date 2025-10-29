Scripts Overview

Root:
- run_backend_smoke.py – quick backend smoke from repo root
- print_backend_routes.py – print backend routes

Backend (flask_backend/scripts):
- bootstrap_env.py – create .env from .env.example
- create_db_if_missing.py – create Postgres DB if missing
- gen_migration.py – autogenerate Alembic migration
- autogen_and_upgrade.py – generate + upgrade to head
- check_alembic_head.py – print Alembic head (CI)
- list_pending_migrations.py – show pending migrations
- verify_models.py – verify metadata & models import
- print_config.py – print Flask config keys
- readiness_check.py – environment and health check
- smoke_health.py – start app briefly and hit /health
- curl_smoke.sh – curl sample endpoints (requires jq)
- curl_smoke_min.sh – curl sample endpoints (no jq)
- dump_openapi.py – fetch and save /openapi.json
- export_seed_data.py – export users/courses/lessons as JSON
- load_seed_data.py – load seed JSON into DB
- export_courses_csv.py – export courses/lessons to CSV
- generate_dummy_data.py – populate demo content
- fetch_config.py – fetch /api/config
- start_compose.sh – launch docker-compose stack
- purge_db.py – drop and recreate tables
- table_counts.py – print table row counts
