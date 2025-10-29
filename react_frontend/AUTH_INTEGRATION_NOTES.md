Auth integration notes

- Registration:
  POST ${VITE_API_BASE_URL}/auth/register
  Body: { "name": "Full Name", "email": "user@example.com", "password": "secret" }
  Response: { user, token }
  Store token (e.g., localStorage) for subsequent requests.

- Login:
  POST ${VITE_API_BASE_URL}/auth/login
  Body: { "email": "user@example.com", "password": "secret" }
  Response: { user, token }

- Protected route example:
  GET ${VITE_API_BASE_URL}/profile/
  Headers: Authorization: Bearer <token from login/register>

- CORS:
  Backend exposes /api/* with CORS enabled (in dev allow-all or ALLOWED_ORIGINS in backend .env).
