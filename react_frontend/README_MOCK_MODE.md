# Mock Mode

This Flutter app is wired to run without any backend when FEATURE_USE_MOCKS=true (default if .env is missing).
- Mock data is provided for Courses and Chat so the Home and Courses screens render content without network calls.
- Authentication uses an in-app mock flow: any email/password logs you in and stores a mock token in shared_preferences.
- Payments use a hosted checkout simulated in a WebView. In mock mode, a local HTML data: URL is loaded; tapping "Pay" returns to the app and unlocks the course.
- To switch to real API calls later, set FEATURE_USE_MOCKS=false in `.env` and implement ApiClient usages in providers/services.

Environment keys in `.env`:
- API_BASE_URL=
- WS_BASE_URL=
- FEATURE_USE_MOCKS=true
- STRIPE_PUBLISHABLE_KEY=
