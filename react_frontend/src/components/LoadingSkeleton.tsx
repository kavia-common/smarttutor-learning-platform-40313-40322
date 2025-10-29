import React from 'react';

interface Props { rows?: number }

// PUBLIC_INTERFACE
const LoadingSkeleton: React.FC<Props> = ({ rows = 3 }) => {
  return (
    <div style={{ display: 'grid', gap: '1rem' }}>
      {Array.from({ length: rows }).map((_, i) => (
        <div key={i} className="card" style={{ padding: '1rem', display: 'flex', gap: '1rem', alignItems: 'center' }}>
          <div style={{ width: 80, height: 80, borderRadius: 12, background: 'rgba(17,24,39,.06)' }} />
          <div style={{ flex: 1 }}>
            <div style={{ width: '40%', height: 14, background: 'rgba(17,24,39,.06)', borderRadius: 6 }} />
            <div style={{ width: '70%', height: 12, background: 'rgba(17,24,39,.06)', borderRadius: 6, marginTop: 8 }} />
          </div>
          <div style={{ width: 80, height: 36, borderRadius: 8, background: 'rgba(17,24,39,.06)' }} />
        </div>
      ))}
    </div>
  );
};

export default LoadingSkeleton;
