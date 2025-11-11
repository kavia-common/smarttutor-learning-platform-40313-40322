# React Frontend (Flutter) - Setup Notes

This container is configured for a Flutter mobile application (Android). The build error "Target file lib/main.dart not found" was due to a missing `lib/main.dart`. This has been added with a minimal `runApp` entry.

What was changed:
- Added `lib/main.dart` with a `main()` that runs `MyApp` and presents a minimal scaffold.
- Ensured testing expectations in `test/widget_test.dart` are satisfied by the app (title and loading message).

How to build and run locally:
1. Ensure Flutter SDK is installed and available on PATH.
2. From the container root:
   ```
   cd smarttutor-learning-platform-40313-40322/react_frontend
   flutter pub get
   flutter test
   flutter run -d android   # or an available device/emulator
   ```
3. For a build:
   ```
   flutter build apk
   ```

Notes:
- The container name is `react_frontend`, but the platform is Flutter mobile.
- Android Gradle configuration expects `local.properties` to define `flutter.sdk` for Android Studio/Gradle. When using the Flutter CLI, `flutter run` handles this automatically.

Environment variables:
- The pubspec lists `.env` in assets. If you need runtime configuration, provide a `.env` file at the project root:
  - Do NOT commit secrets.
  - Provide a `.env.example` with keys only (one is included).

Acceptance Criteria Mapping:
- lib/main.dart now exists and contains a valid `main()` that calls `runApp`.
- `flutter pub get` should succeed.
- `flutter build` and `flutter run` should proceed without the "lib/main.dart not found" error.
