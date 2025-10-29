# SmartTutor Monorepo

Components:
- Frontend: smarttutor-learning-platform-40313-40322/react_frontend
- Backend:  smarttutor-learning-platform-40313-40322/flask_backend

Quickstarts:
- Frontend: see react_frontend/README.md and .env.example
- Backend:  see BACKEND_QUICKSTART.md (root) and flask_backend/README.md

Integration:
- See INTEGRATION_README.md and FRONTEND_BACKEND_ENV.md

Container/deployment:
- docker-compose.yml to run Postgres + Flask backend locally
- flask_backend/Dockerfile builds the backend container

Diagnostics:
- Backend diagnostics and test instructions: flask_backend/DIAGNOSTICS.md, TESTING.md
- OpenAPI: http://localhost:8000/openapi.json (when backend is running)
