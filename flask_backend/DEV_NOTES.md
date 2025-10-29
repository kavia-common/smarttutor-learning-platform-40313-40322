# Development Notes

- Create and activate venv:
  python -m venv .venv && source .venv/bin/activate

- Install runtime deps:
  pip install -r requirements.txt

- Install dev/test deps (optional):
  pip install -r requirements-dev.txt

- Run tests:
  python scripts/run_tests.py

- Start server:
  python run_dev.py
  # or:
  bash run.sh
