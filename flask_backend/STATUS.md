# Backend Status Checklist

After setup, verify these quickly:

- Config
  - .env present with DATABASE_URL and JWT_SECRET
  - alembic upgrade head succeeds

- Health and docs
  - GET /health -> 200
  - GET /openapi.json -> 200 and valid JSON
  - GET /docs/openapi.html -> renders Redoc

- Diagnostics
  - GET /diag/ping -> 200
  - GET /diag/version -> 200

- Data endpoints (after seeding)
  - GET /api/users -> 200 with items
  - GET /api/courses -> 200 with items
  - GET /api/lessons -> 200 with items
  - GET /api/enrollments -> 200 with items
  - GET /api/payments -> 200 with items
  - GET /api/recommendations/cache -> 200 with items
  - GET /api/whiteboard/sessions -> 200 (empty or with items)

Tools:
- python scripts/ping_all_endpoints.py
- bash scripts/core_curl_examples.sh
- make ping-all
