# SmartTutor Backend Quick Intro

Run the backend:
- cd flask_backend
- cp .env.example .env
- python -m venv .venv && source .venv/bin/activate
- pip install -r requirements.txt
- alembic upgrade head
- python run_dev.py  # serves on http://localhost:8000

Frontend env:
- Set VITE_API_BASE_URL=http://localhost:8000
- Set VITE_WS_BASE_URL=ws://localhost:8000 (placeholder until WS is implemented)

Diagnostics endpoints:
- /health
- /api/status, /api/version
- /api/time, /api/echo
- /api/uptime, /api/memory, /api/metrics, /api/proc, /api/cpu, /api/routes
- /openapi.json
