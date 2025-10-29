# Flutter Tooling in Hybrid Repo

This monorepo contains a Flutter-based template within `react_frontend/`. Some CI analyzers require the Flutter project root.

Ways to run tooling:
- From repo root using wrapper:
  ./flutterw analyze
  ./flutterw pub get
  ./flutterw test

- Directly from the project directory:
  cd smarttutor-learning-platform-40313-40322/react_frontend
  flutter pub get
  flutter analyze

We include `.metadata` and `.flutter_root` to assist root detection.
