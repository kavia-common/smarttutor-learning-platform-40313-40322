# SmartTutor – Monorepo

This workspace contains:
- React Frontend (Vite + TypeScript): smarttutor-learning-platform-40313-40322/react_frontend
- Flask Backend (PostgreSQL + SQLAlchemy + Alembic): smarttutor-learning-platform-40313-40322/flask_backend

Quick start (local without Docker)

Frontend (React):
1) cd smarttutor-learning-platform-40313-40322/react_frontend
2) cp .env.example .env
   - Set VITE_API_BASE_URL (e.g., http://localhost:8000/api)
   - Set VITE_WS_BASE_URL (e.g., ws://localhost:8000)
   - Set VITE_STRIPE_PK (publishable key)
3) npm install
4) npm run dev  # http://localhost:3000

Backend (Flask):
1) cd smarttutor-learning-platform-40313-40322/flask_backend
2) cp .env.example .env  # Update DATABASE_URL, JWT_SECRET, STRIPE_SK, CORS_ORIGINS
3) python -m venv .venv && . .venv/bin/activate
4) pip install -r requirements.txt
5) alembic upgrade head  # applies initial migration
6) python seed.py        # optional – adds sample users, course, and lessons
7) python wsgi.py        # http://localhost:8000/health

Docker Compose (recommended for full stack)
1) cd smarttutor-learning-platform-40313-40322
2) Copy backend env:
   cp flask_backend/.env.example flask_backend/.env
   - Ensure CORS_ORIGINS includes http://localhost:3000
3) Build and start:
   docker compose up --build
   - Frontend: http://localhost:3000
   - Backend:  http://localhost:8000 (health: /health, OpenAPI: /openapi.json)
   - Postgres: localhost:5432
4) Apply migrations/seed happen automatically on backend container start (seed is best-effort).

E2E Verification Checklist
- Register/Login:
  1) In the frontend, go to Register and create a new account.
  2) Login with the new credentials and verify Profile shows your user info.
- Catalog:
  1) Navigate to Catalog and confirm course list renders.
- Course session:
  1) Open a course to view the 3-panel layout (video, whiteboard, chat).
  2) Send a chat message and draw on whiteboard (if supported by backend WS).
- Real-time (chat/whiteboard):
  1) Open the same course in two browser windows.
  2) Verify chat and whiteboard events sync in real-time via WS base url (VITE_WS_BASE_URL).
- Payments:
  1) Go to Checkout for a course.
  2) Create a payment intent from the frontend (calls backend /api/payments/intent).
  3) Verify a client secret is returned and the intent appears in logs if Stripe test keys are configured.

Seeding data
- The backend image runs alembic upgrade head on startup and attempts python seed.py.
- You can run additional seeds inside the backend container:
  docker compose exec backend python seed.py

Docs:
- BACKEND_QUICK_START.md – backend setup
- INTEGRATION_CHECKLIST.md – end-to-end wiring
- CI_GUIDANCE.md – configure CI to use React app, not Flutter

Note:
Some Flutter scaffolding exists in react_frontend/, but the active web app is React. Configure CI to build the React app and test the Flask backend to avoid "Flutter project root" errors.
