# smarttutor-learning-platform-40313-40322

SmartTutor – React frontend (Vite + TypeScript) initialized in `react_frontend/`.

How to run:
1. cd react_frontend
2. Copy .env.example to .env and update variables
3. npm install
4. npm run dev
   - App will be served on http://localhost:3000

Acceptance criteria implemented:
- Dev server on port 3000
- Top navigation with links to Login and Catalog
- Catalog page with placeholder course cards and AI recommendations sidebar
- Course page with 3-panel layout (video left, whiteboard center, chat right)
- .env.example includes VITE_API_BASE_URL, VITE_WS_BASE_URL, VITE_STRIPE_PK
