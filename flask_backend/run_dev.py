import os
from app import create_app

# PUBLIC_INTERFACE
def main():
    """Run the Flask app in development mode on PORT (default 8000)."""
    app = create_app()
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=True)

if __name__ == "__main__":
    main()
