# Environment Variables

Backend (flask_backend/.env):
- DATABASE_URL: SQLAlchemy URL (prefer postgresql+psycopg)
- JWT_SECRET: Random long string for JWT signing
- PORT: default 8000

Frontend (react_frontend/.env):
- VITE_API_BASE_URL: e.g. http://localhost:8000
- VITE_WS_BASE_URL: e.g. ws://localhost:8000
- VITE_STRIPE_PK: your Stripe publishable key for local testing
