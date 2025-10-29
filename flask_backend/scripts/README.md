# Backend Scripts

Utilities to aid development and diagnostics.

Diagnostics:
- check_core_endpoints.py — ping core routes to ensure they return 200
- print_env_and_service.py — print environment and route count
- dump_routes.py — list routes (if present)
- versions_info.py — print dependency versions (if present)

OpenAPI:
- generate_openapi_site.py — fetch /openapi.json and save to docs/openapi.json
- serve_docs.py — serve docs/ locally on port 8080

Seeding:
- seed.py — minimal development seed
- seed_all_sample.py — fuller seed if present
- seed_enrollment.py — enrollments data if present

Fetchers:
- fetch_receipt.py — GET /api/payments/{id}
- fetch_whiteboard_sessions.py — list sessions (if present)
- fetch_whiteboard_events.py — list events (if present)
