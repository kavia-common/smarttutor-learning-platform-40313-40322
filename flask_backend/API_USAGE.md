# SmartTutor Backend API Usage

Base URL: http://localhost:8000

Core
- GET /            — API index with helpful links
- GET /health      — Health check
- GET /openapi.json — OpenAPI specification (merged with extras)

Diagnostics
- GET /diag/ping      — Simple ping returning {"pong": true}
- GET /diag/headers   — Echo request headers (useful when debugging proxies)
- GET /diag/alembic   — Simple Alembic status placeholder
- GET /diag/version   — App version and env presence checks

Whiteboard
- GET /api/whiteboard/sessions
  - Optional query: course_id=<int>
- GET /api/whiteboard/sessions/{session_id}/events

Payments
- GET /api/payments — Placeholder (not implemented)
- GET /api/payments/{payment_id} — Read-only dev receipt object

Notes
- Ensure DATABASE_URL and JWT_SECRET are configured in flask_backend/.env.
- CORS is permissive for local dev; tighten before production.
- For a browsable UI of OpenAPI, open flask_backend/docs/openapi.html after generating docs:
  python scripts/generate_openapi_site.py
  python scripts/serve_docs.py  # opens at http://localhost:8080
