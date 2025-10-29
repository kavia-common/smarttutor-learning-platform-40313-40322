from .wsgi import get_app

def main():
    app = get_app()
    # Running via python -m flask_backend should just expose app object for WSGI servers.
    # For ad-hoc runs, suggest using run_dev.py.
    print("SmartTutor Flask backend package. Use `python run_dev.py` to run the dev server.")
    return app

if __name__ == "__main__":
    main()
