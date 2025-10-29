Hybrid repository layout notice

This repository contains:
- A React (Vite + TypeScript) web app at smarttutor-learning-platform-40313-40322/react_frontend (with some Flutter boilerplate files from a prior template).
- A Flask backend at smarttutor-learning-platform-40313-40322/flask_backend.

Some CI analyzers that expect a pure Flutter project may mis-detect the root. If your CI step runs Flutter analysis:
- Set the working directory to smarttutor-learning-platform-40313-40322/react_frontend
- Or skip Flutter tasks if building the React web app variant.

We include a minimal .metadata in react_frontend to aid root detection.
