# CI Troubleshooting (Hybrid Repo)

Symptom: "Could not determine project root directory for Flutter project"

Cause: This repository contains a React frontend with some Flutter template files. CI analyzers expecting a pure Flutter layout may mis-detect the root.

Resolution options:
- Point Flutter tasks to the correct directory:
  cd smarttutor-learning-platform-40313-40322/react_frontend
  flutter analyze
- Or skip Flutter analysis if building the React web app variant.
- Use provided helpers:
  - ./flutterw analyze
  - make flutter-root

Ensure your CI job sets the working directory to the React frontend if Flutter steps are required.
