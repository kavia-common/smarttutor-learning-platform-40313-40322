# SmartTutor E2E Verification

Prereqs:
- Stripe test keys configured:
  - Frontend: VITE_STRIPE_PK in react_frontend/.env
  - Backend: STRIPE_SK in flask_backend/.env
- Database initialized (compose does this automatically)

Steps:
1) Start stack
   docker compose up --build
   - Frontend: http://localhost:3000
   - Backend:  http://localhost:8000

2) Register & Login
   - In UI, register a user and then login.
   - Confirm Profile shows the logged in user.

3) Catalog
   - Navigate to Catalog.
   - Confirm sample courses are listed.

4) Course Session
   - Open a course and verify 3-panel layout (video, whiteboard, chat).

5) Real-time
   - Open the same course in two browser windows.
   - Verify chat messages and whiteboard events sync if WS is enabled.

6) Payment Intent
   - Navigate to Checkout for a course.
   - Trigger "Create Payment Intent" from UI.
   - Verify client secret is returned and no server error occurs.

Troubleshooting:
- 401 Unauthorized: Ensure JWT token is stored and sent; re-login if needed.
- CORS errors: Update flask_backend/.env CORS_ORIGINS to include http://localhost:3000.
- DB connection errors: Ensure Postgres is healthy (docker compose ps) and DATABASE_URL points to db service.
