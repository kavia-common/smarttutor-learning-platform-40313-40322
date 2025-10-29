# Authentication Roadmap

Current state:
- No authentication is enforced. Development endpoints are read-only and intended for diagnostics.

Next steps:
1) Choose JWT library:
   - PyJWT or Authlib for robust JWT creation/verification.
2) Middleware:
   - Add a before_request hook to parse Authorization: Bearer <token>
   - Attach current_user to Flask g context after verification
3) Protected endpoints:
   - Require auth for POST/PUT/PATCH/DELETE in future APIs (e.g., chat posts, whiteboard actions)
4) Token issuance:
   - Add /auth/login to validate credentials and issue JWT
   - Add /auth/refresh for token rotation
5) Password hashing:
   - Use Werkzeug's generate_password_hash and check_password_hash
6) CSRF/CORS:
   - Keep CORS permissive in dev. Lockdown allowed origins for production
7) Secrets:
   - JWT_SECRET configured via environment only (.env), do not hardcode

References:
- app/jwt_utils.py — lightweight placeholder; replace with PyJWT/Authlib for production
