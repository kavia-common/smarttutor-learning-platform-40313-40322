Backend Smoke – One-command checks

From repo root:
- python smarttutor-learning-platform-40313-40322/run_backend_smoke.py

From backend folder:
- python scripts/smoke_all_in_one.py
  - Starts server briefly
  - Hits core endpoints (/health, /api/status, /api/ping, /api/time, etc.)
  - Exits with non-zero on failures

Other useful quick checks:
- python scripts/check_all_endpoints.py
- bash scripts/curl_smoke_min.sh
- python scripts/validate_openapi.py
