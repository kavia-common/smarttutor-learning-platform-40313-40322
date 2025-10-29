# React Frontend (Hybrid Scaffold Notice)

This directory contains a React (Vite + TypeScript) web app alongside some Flutter template files that may be present due to initial scaffolding. Treat this as a React app for local development.

Quick start:
1) cp .env.example .env
2) npm install
3) npm run dev
   - App runs at http://localhost:3000

Backend integration:
- The Flask backend should be running at http://localhost:8000
- Ensure .env contains VITE_API_BASE_URL and VITE_WS_BASE_URL pointing to the backend
