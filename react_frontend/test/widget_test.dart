import 'package:flutter_test/flutter_test.dart';
import 'package:react_frontend/main.dart';

void main() {
  testWidgets('App builds and shows title', (tester) async {
    await tester.pumpWidget(const SmartTutorApp());
    expect(find.text('SmartTutor'), findsOneWidget);
  });
}
