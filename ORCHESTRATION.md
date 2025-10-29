SmartTutor Orchestration Guide

Containers:
- Frontend (React + Vite): smarttutor-learning-platform-40313-40322/react_frontend
- Backend (Flask): smarttutor-learning-platform-40313-40322/flask_backend

Local development (without Docker):
1) Backend
   - cd smarttutor-learning-platform-40313-40322/flask_backend
   - cp .env.example .env
     DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/smarttutor
     JWT_SECRET=use_a_long_random_value
   - python -m venv .venv && source .venv/bin/activate
   - pip install -r requirements.txt
   - python init_db.py
   - python run_dev.py
   - Health: http://localhost:8000/health
   - API root: http://localhost:8000/api/
   - OpenAPI: http://localhost:8000/openapi.json

2) Frontend
   - cd smarttutor-learning-platform-40313-40322/react_frontend
   - cp .env.example .env
     VITE_API_BASE_URL=http://localhost:8000/api
     VITE_WS_BASE_URL=ws://localhost:8000/ws
     VITE_STRIPE_PK=pk_test_change_me
   - npm install
   - npm run dev
   - App served at http://localhost:3000

Using Docker for Backend:
- cd smarttutor-learning-platform-40313-40322/flask_backend
- cp .env.example .env  (optional; docker-compose provides sane defaults)
- docker compose up --build
- Backend: http://localhost:8000

Notes:
- The CI mobile analysis error referencing a Flutter project root is unrelated since the UI is a React app. Point CI to react_frontend for web builds or keep Flutter checks disabled for this workspace.
- Do not hardcode secrets; always use environment variables (.env files only for local development).
