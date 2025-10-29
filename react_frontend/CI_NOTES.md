CI Notes for React Frontend

- This repository contains Flutter scaffolding files; however, the active web frontend is React (Vite + TypeScript).
- Configure your CI to:
  1) cd smarttutor-learning-platform-40313-40322/react_frontend
  2) cp .env.example .env
  3) npm ci
  4) npm run build

- Avoid running Flutter analysis/build steps unless explicitly targeting a separate Flutter pipeline.
- Backend is in: smarttutor-learning-platform-40313-40322/flask_backend (see CI_GUIDANCE.md for steps).
