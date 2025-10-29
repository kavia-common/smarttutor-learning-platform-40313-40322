# Payments API (Development)

Endpoints:
- GET /api/payments
  - Query:
    - user_id (optional)
    - course_id (optional)
    - status (optional: succeeded, pending, failed)
    - limit, offset (pagination)
- GET /api/payments/{payment_id}
  - Returns a basic receipt-like payload with joined user and course

Examples:
- List all payments:
  curl http://localhost:8000/api/payments

- Filter by user:
  curl "http://localhost:8000/api/payments?user_id=1"

- Fetch a payment receipt:
  curl http://localhost:8000/api/payments/1
