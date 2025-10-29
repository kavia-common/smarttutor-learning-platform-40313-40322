# Environment variables (Flask Backend)

Required:
- DATABASE_URL: SQLAlchemy URL to PostgreSQL. Example: postgresql+psycopg://postgres:password@localhost:5432/smarttutor
- JWT_SECRET: Random string used for JWT signing.

Optional:
- APP_VERSION: Version string to surface in diagnostics and OpenAPI info.
- PORT: Flask run port. Default: 8000.

Notes:
- Do not commit real secrets. Use .env locally (copy from .env.example).
- For CI, supply env via the runner.
