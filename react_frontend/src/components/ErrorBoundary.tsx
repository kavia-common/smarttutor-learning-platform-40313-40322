import React from 'react';

type State = { hasError: boolean; message?: string };

// PUBLIC_INTERFACE
export class ErrorBoundary extends React.Component<React.PropsWithChildren, State> {
  constructor(props: React.PropsWithChildren) {
    super(props);
    this.state = { hasError: false, message: undefined };
  }

  static getDerivedStateFromError(error: any): State {
    return { hasError: true, message: String(error?.message || error) };
  }

  componentDidCatch(error: any) {
    // eslint-disable-next-line no-console
    console.error('ErrorBoundary caught:', error);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="card" style={{ padding: '1rem', marginTop: '1rem', color: '#B91C1C', background: 'rgba(239,68,68,0.06)' }}>
          <strong>Something went wrong.</strong>
          <div style={{ marginTop: '.5rem' }}>{this.state.message}</div>
        </div>
      );
    }
    return this.props.children;
  }
}
