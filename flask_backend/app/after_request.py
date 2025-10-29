from flask import Flask

# PUBLIC_INTERFACE
def register_after_request(app: Flask) -> None:
    """Register after_request hook to include environment/version headers."""
    @app.after_request
    def add_env_headers(resp):
        resp.headers.setdefault("X-Env", "dev")
        resp.headers.setdefault("X-App-Version", app.config.get("APP_VERSION", "0.1.0"))
        return resp
