# react_frontend

A React (Vite + TypeScript) web app scaffold.

Backend integration:
- Configure VITE_API_BASE_URL in .env (see .env.example), e.g. http://localhost:8000/api
- Configure VITE_WS_BASE_URL for websockets, e.g. ws://localhost:8000
- Configure VITE_STRIPE_PK for Stripe publishable key

Run locally:
- cp .env.example .env
- npm install
- npm run dev  # http://localhost:3000

Run via Docker Compose:
- From workspace root: docker compose up --build
- Frontend will be available at http://localhost:3000 (served by Nginx from built assets)
- Make sure backend CORS_ORIGINS includes http://localhost:3000
