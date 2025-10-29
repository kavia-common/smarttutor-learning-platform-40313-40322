CI Hints

- Frontend is a React (Vite + TypeScript) web app located at:
  smarttutor-learning-platform-40313-40322/react_frontend

- Do not run Flutter analyzers or expect a Flutter project root here.
  If a mobile analyzer is required, skip or point to the React web app.

- Backend is a Flask app located at:
  smarttutor-learning-platform-40313-40322/flask_backend

Suggested CI steps:
1) Backend (optional):
   cd smarttutor-learning-platform-40313-40322/flask_backend
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt -r requirements.dev.txt
   pytest

2) Frontend:
   cd smarttutor-learning-platform-40313-40322/react_frontend
   npm ci
   npm run build
