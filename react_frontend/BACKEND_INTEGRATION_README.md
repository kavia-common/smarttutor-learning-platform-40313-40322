React ↔ Flask Backend Integration

New utilities:
- src/api/backend.ts – functions to call backend REST API
- src/api/hooks.ts – useCourses() to fetch courses with optional pagination
- src/api/authStore.ts – localStorage token storage helpers
- src/api/auth.ts – helper to build Authorization headers
- src/api/protected.ts – example protected endpoint call (profile)

Pages updated:
- Catalog.tsx – shows backend courses when available (fallback to placeholders)
- Register.tsx – registers via /api/auth/register and stores token
- Login.tsx – logs in via /api/auth/login and stores token
- Profile.tsx – fetches /api/profile/ with Bearer token and renders user info

Environment:
- .env example includes:
  VITE_API_BASE_URL=http://localhost:8000/api
  VITE_WS_BASE_URL=ws://localhost:8000/ws

Next steps (suggested):
- Display signed-in state in NavBar and add sign-out
- Use backend lessons on Course page
- Integrate recommendations /api/recommendations/ and payments POST /api/payments/ (dev stub)
