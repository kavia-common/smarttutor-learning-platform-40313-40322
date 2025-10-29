import React from 'react';

// PUBLIC_INTERFACE
const Checkout: React.FC = () => {
  return (
    <div className="container" style={{ maxWidth: 680 }}>
      <div className="card" style={{ padding: '1rem', marginTop: '1rem' }}>
        <h2 style={{ marginTop: 0 }}>Checkout</h2>
        <p style={{ color: '#6B7280' }}>Stripe integration will be wired here using VITE_STRIPE_PK.</p>
      </div>
    </div>
  );
};

export default Checkout;
