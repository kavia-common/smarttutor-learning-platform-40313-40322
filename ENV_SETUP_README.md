Environment setup quick reference

Backend:
- Copy smarttutor-learning-platform-40313-40322/flask_backend/.env.example to .env
- Ensure DATABASE_URL and JWT_SECRET are set
- For Docker Compose:
  docker compose up --build -d
  docker compose exec backend alembic upgrade head
  docker compose exec backend python seed.py

Frontend:
- cd smarttutor-learning-platform-40313-40322/react_frontend
- cp .env.example .env
- npm install && npm run dev
