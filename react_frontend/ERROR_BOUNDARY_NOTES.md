Wrap your application with the ErrorBoundary to catch runtime errors:

import { ErrorBoundary } from '@components/ErrorBoundary';

<ErrorBoundary>
  <App />
</ErrorBoundary>

You can progressively adopt it around specific pages or sections.
