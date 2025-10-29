Wiring notes for React frontend to Flask backend

- API base URL is read from VITE_API_BASE_URL (see .env.example).
- Use src/api/backend.ts for REST calls:
  - apiCourses(), apiCourseDetail(), apiLessons()
  - apiRegister(), apiLogin(), apiProfile()
  - apiHealth(), apiStatus()

- Example (Catalog page):
  import { useCourses } from '@api/hooks';
  const { items, loading, error } = useCourses(12);

  Replace placeholder course list with 'items' from the hook when ready.

- Auth:
  After login/register, store 'token' (e.g., localStorage) and call apiProfile(token).

- WebSocket:
  Will be added later under /ws endpoints; see docs at backend /docs/ws.
