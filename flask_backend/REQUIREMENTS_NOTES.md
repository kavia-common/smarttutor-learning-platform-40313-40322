Requirements Notes

- Flask-Cors is included because the backend enables CORS for /api/* to allow the React frontend to call APIs during development.
- psycopg[binary] is used for convenience; if building for Alpine, consider switching to source build or ensure libpq is available.
