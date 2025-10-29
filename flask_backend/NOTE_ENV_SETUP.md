# Environment Setup Note

Remember to copy .env.example to .env in this directory before running the app or migrations:

cp .env.example .env

Required variables:
- DATABASE_URL (PostgreSQL SQLAlchemy URL with psycopg driver)
- JWT_SECRET (random long string)
Optional:
- PORT (default 8000)
