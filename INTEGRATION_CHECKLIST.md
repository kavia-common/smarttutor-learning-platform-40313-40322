Integration Checklist (Frontend ↔ Backend)

Backend (Flask):
- [x] Models and Alembic migrations (PostgreSQL preferred)
- [x] Seed data and dev scripts
- [x] REST endpoints (users, courses, lessons, enrollments, chat read, whiteboard read, payments read/write stub, recommendations read/write stub)
- [x] Auth (register, login, profile), JWT decorator
- [x] OpenAPI docs and download endpoint
- [x] Dockerfile + docker-compose for Postgres
- [x] Tests: health, status, auth, version/openapi

Frontend (React + Vite):
- [x] API base environment (.env.example)
- [x] API client wrappers and hooks
- [x] Catalog uses backend courses (fallback to placeholders)
- [x] Register/Login wired to backend; token persisted; Profile fetches protected endpoint
- [ ] Add route guards for protected pages
- [ ] Show signed-in state in NavBar and sign-out
- [ ] Use backend lessons on Course page
- [ ] Integrate payments create stub for dev checkout
- [ ] Render recommendations from /api/recommendations/
- [ ] Replace placeholders with loading skeletons and error toasts

CI:
- [x] run_ci.sh includes backend tests + frontend build
- [ ] Ensure CI uses React web app path (react_frontend) and skips Flutter analyzers

Notes:
- Configure ALLOWED_ORIGINS in backend .env for stricter CORS in non-dev.
- For production, replace payment stub with real gateway and add robust auth flows (refresh, logout, CSRF for forms if needed).
