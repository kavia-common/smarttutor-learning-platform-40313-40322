# Backend Endpoints (Summary)

System/Diagnostics:
- GET /                -> index payload with links
- GET /health          -> { status: "ok" }
- GET /openapi.json    -> OpenAPI document
- GET /api/status      -> backend name/version ok flag
- GET /api/version     -> version only
- GET /api/routes      -> list registered routes
- GET /api/uptime      -> service uptime
- GET /api/memory      -> memory RSS (Linux)
- GET /api/metrics     -> in-memory request counters
- GET /api/proc        -> pid and thread count
- GET /api/cpu         -> CPU count and load averages
- GET /api/time        -> server UTC time
- GET/POST /api/echo   -> echo request info
- GET /api/headers     -> sanitized request headers
- GET /api/ws-help     -> placeholder WS docs

Core data (read-only):
- GET /api/users
- GET /api/users/{user_id}
- GET /api/courses
- GET /api/courses/{course_id}/lessons
- GET /api/users/{user_id}/enrollments
- GET /api/users/{user_id}/payments
- GET /api/users/{user_id}/recommendations

Dev helpers (non-production):
- POST /api/dev/enroll  body: { user_id, course_id }

Notes:
- See app/openapi_register.py to view how extra path modules are merged.
- See DIAGNOSTICS.md for scripts to inspect and verify endpoints.
