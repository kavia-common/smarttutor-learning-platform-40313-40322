# Diagnostics Scripts

Run backend first (see QUICK_START.md), then use:

- python scripts/run_all_diagnostics.py
  - Hits key endpoints and validates JSON
- python scripts/validate_openapi.py
  - Fetches /openapi.json and validates basic keys
- python scripts/openapi_summary.py
  - Prints tags and first few paths from /openapi.json
- python scripts/fetch_routes.py
  - Shows registered routes
- python scripts/check_headers.py
  - Prints X-App-Version and X-Env response headers from /api/headers
- python scripts/bench_endpoints.py
  - Quick latency check for diagnostics endpoints
- python scripts/diagnostics_cli.py
  - Orchestrates multiple checks (env, alembic, models, counts, smoke)
