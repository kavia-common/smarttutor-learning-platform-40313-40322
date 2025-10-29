import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { apiLogin, apiProfile } from '@api/backend';
import { saveToken } from '@api/authStore';

// PUBLIC_INTERFACE
const Login: React.FC = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [pwd, setPwd] = useState('');
  const [err, setErr] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    setErr(null);
    if (!email.trim() || !pwd.trim()) {
      setErr('Please enter email and password');
      return;
    }
    setLoading(true);
    try {
      const res = await apiLogin(email.trim(), pwd);
      saveToken(res.token);
      // Optionally verify token by fetching profile (ignore failure)
      try {
        await apiProfile(res.token);
      } catch {}
      navigate('/profile');
    } catch (e: any) {
      setErr(e?.message || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container" style={{ maxWidth: 480 }}>
      <div className="card" style={{ padding: '1.5rem', marginTop: '1rem' }}>
        <h1 style={{ margin: 0 }}>Login</h1>
        <p style={{ color: '#6B7280' }}>Welcome back to SmartTutor</p>
        <form style={{ display: 'grid', gap: '.75rem', marginTop: '1rem' }} onSubmit={(e) => { e.preventDefault(); submit(); }}>
          <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" type="email" style={{ padding: '.7rem .9rem', borderRadius: 10, border: '1px solid rgba(17,24,39,.12)' }} />
          <input value={pwd} onChange={(e) => setPwd(e.target.value)} placeholder="Password" type="password" style={{ padding: '.7rem .9rem', borderRadius: 10, border: '1px solid rgba(17,24,39,.12)' }} />
          <button disabled={loading} type="submit" className="btn btn-primary">{loading ? 'Signing in...' : 'Sign in'}</button>
          {err && <div style={{ color: '#B91C1C' }}>{err}</div>}
        </form>
        <div style={{ marginTop: '.75rem' }}>
          <small>New here? <Link to="/register" style={{ color: 'var(--color-primary)' }}>Create an account</Link></small>
        </div>
      </div>
    </div>
  );
};

export default Login;
