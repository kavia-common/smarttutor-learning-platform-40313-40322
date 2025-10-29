import React, { useEffect, useState } from 'react';
import { getToken, clearToken } from '@api/authStore';
import { apiProfile } from '@api/backend';

// PUBLIC_INTERFACE
const Profile: React.FC = () => {
  const [data, setData] = useState<{ id: number; email: string; name: string; role: string } | null>(null);
  const [error, setError] = useState<string | null>(null);
  const token = getToken();

  useEffect(() => {
    let cancelled = false;
    if (!token) {
      setError('Not signed in');
      return;
    }
    apiProfile(token)
      .then((res) => {
        if (!cancelled) setData(res);
      })
      .catch((e) => {
        if (!cancelled) setError(String(e?.message || e));
      });
    return () => {
      cancelled = true;
    };
  }, [token]);

  return (
    <div className="container">
      <div className="card" style={{ padding: '1rem', marginTop: '1rem' }}>
        <h2 style={{ marginTop: 0 }}>Profile</h2>
        {!token && <p style={{ color: '#6B7280' }}>Please sign in to view your profile.</p>}
        {token && !data && !error && <p style={{ color: '#6B7280' }}>Loading your profile...</p>}
        {error && <p style={{ color: '#B91C1C' }}>{error}</p>}
        {data && (
          <div style={{ display: 'grid', gap: '.35rem' }}>
            <div><strong>Name:</strong> {data.name}</div>
            <div><strong>Email:</strong> {data.email}</div>
            <div><strong>Role:</strong> {data.role}</div>
            <button className="btn btn-ghost" style={{ marginTop: '.5rem' }} onClick={() => { clearToken(); window.location.reload(); }}>Sign out</button>
          </div>
        )}
      </div>
    </div>
  );
};

export default Profile;
