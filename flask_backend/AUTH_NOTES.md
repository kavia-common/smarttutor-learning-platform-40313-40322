Auth scaffold

- Password hashing:
  Use app.security.hash_password() to hash plaintext before storing in users.password_hash.
  Verify via app.security.verify_password().

- Minimal JWT (HS256):
  Use app.security.create_jwt({"sub": user_id}, JWT_SECRET, expires_in=3600)
  Verify via app.security.verify_jwt(token, JWT_SECRET)

Next steps (future task):
- Add /api/auth/register and /api/auth/login routes:
  - Register: create user with hashed password, return basic profile + token
  - Login: verify password, return token
- Add @login_required decorator to protect endpoints (read JWT from Authorization: Bearer)
- Replace simple PBKDF2 with passlib[bcrypt] for production
- Rotate JWT_SECRET via environment, never hardcode
