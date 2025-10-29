Service Manifest - Flask Backend

Service name: smarttutor-backend
Language/Framework: Python 3.11 / Flask 3.x
Port(s): 8000 (HTTP)

Health/Diagnostics:
- GET /health            -> 200 OK
- GET /api/status        -> 200 OK (counts)
- GET /api/version       -> 200 OK (name, version)
- GET /openapi.json      -> 200 OK

Primary API base: /api
Auth:
- POST /api/auth/register
- POST /api/auth/login
- GET  /api/profile/ (Bearer token)

Notes:
- Requires DATABASE_URL and JWT_SECRET in environment (.env for local)
- CORS configured for /api/*; override with ALLOWED_ORIGINS
- Prefer PostgreSQL: postgresql+psycopg://user:pass@host:5432/dbname
