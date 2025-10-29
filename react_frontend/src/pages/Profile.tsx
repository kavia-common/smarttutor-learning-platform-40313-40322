import React from 'react';

// PUBLIC_INTERFACE
const Profile: React.FC = () => {
  return (
    <div className="container">
      <div className="card" style={{ padding: '1rem', marginTop: '1rem' }}>
        <h2 style={{ marginTop: 0 }}>Profile</h2>
        <p style={{ color: '#6B7280' }}>User details and settings will appear here.</p>
      </div>
    </div>
  );
};

export default Profile;
