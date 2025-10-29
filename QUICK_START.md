SmartTutor – Quick Start

Backend (Flask):
1) cd smarttutor-learning-platform-40313-40322/flask_backend
2) python -m venv .venv && . .venv/bin/activate
3) cp .env.example .env  # set DATABASE_URL + JWT_SECRET
4) pip install -r requirements.txt
5) alembic upgrade head
6) python seed.py  # optional
7) python wsgi.py  # http://localhost:8000/health

Frontend (React Vite):
1) cd smarttutor-learning-platform-40313-40322/react_frontend
2) cp .env.example .env
3) npm install
4) npm run dev  # http://localhost:3000

Notes:
- Ignore Flutter-related CI warnings; the active web app is React. Configure CI per CI_GUIDANCE.md and CI_OVERRIDE_NOTES.md.
- For quick backend smoke without Postgres, use SQLite fallback:
  cd flask_backend && python run_sqlite_dev.py
