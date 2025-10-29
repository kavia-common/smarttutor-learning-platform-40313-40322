# Frontend <-> Backend Environment Linkage

Frontend (react_frontend/.env):
- VITE_API_BASE_URL=http://localhost:8000
- VITE_WS_BASE_URL=ws://localhost:8000
- VITE_STRIPE_PK=pk_test_1234567890 (placeholder)

Backend (flask_backend/.env):
- DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/smarttutor
- JWT_SECRET=<your secret>
- APP_VERSION=0.1.0
- PORT=8000

Notes:
- Ensure backend is running on port 8000 before starting the frontend.
- Update VITE_API_BASE_URL if backend runs on a different host/port.
- CORS headers are enabled permissively for development in the backend.
