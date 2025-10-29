import React from 'react';
import { Link } from 'react-router-dom';

// PUBLIC_INTERFACE
const Login: React.FC = () => {
  return (
    <div className="container" style={{ maxWidth: 480 }}>
      <div className="card" style={{ padding: '1.5rem', marginTop: '1rem' }}>
        <h1 style={{ margin: 0 }}>Login</h1>
        <p style={{ color: '#6B7280' }}>Welcome back to SmartTutor</p>
        <form style={{ display: 'grid', gap: '.75rem', marginTop: '1rem' }}>
          <input placeholder="Email" type="email" style={{ padding: '.7rem .9rem', borderRadius: 10, border: '1px solid rgba(17,24,39,.12)' }} />
          <input placeholder="Password" type="password" style={{ padding: '.7rem .9rem', borderRadius: 10, border: '1px solid rgba(17,24,39,.12)' }} />
          <button type="button" className="btn btn-primary">Sign in</button>
        </form>
        <div style={{ marginTop: '.75rem' }}>
          <small>New here? <Link to="/register" style={{ color: 'var(--color-primary)' }}>Create an account</Link></small>
        </div>
      </div>
    </div>
  );
};

export default Login;
