# Diagnostics Quick Run-Book

With backend running on http://localhost:8000:

- Basic smoke:
  python scripts/smoke_basic.py

- Full diagnostics:
  python scripts/run_all_diagnostics.py
  python scripts/diagnostics_cli.py

- OpenAPI:
  python scripts/validate_openapi.py
  python scripts/openapi_summary.py
  python scripts/publish_openapi.py

- DB checks:
  python scripts/check_env_vars.py
  python scripts/alembic_info.py
  python scripts/check_db_connection.py
  python scripts/show_pending_diffs.py

- Routes:
  python scripts/fetch_routes.py
  python scripts/dump_routes.py
