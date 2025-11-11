# Mock Mode

This Flutter app is wired to run without any backend when FEATURE_USE_MOCKS=true (default if .env is missing).
- Mock data is provided for Courses and Chat so the Home and Courses screens render content without network calls.
- To switch to real API calls later, set FEATURE_USE_MOCKS=false in `.env` and implement ApiClient usages in providers.

Environment keys in `.env`:
- API_BASE_URL=
- WS_BASE_URL=
- FEATURE_USE_MOCKS=true
- STRIPE_PUBLISHABLE_KEY=
