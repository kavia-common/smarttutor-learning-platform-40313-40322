import React from 'react';

interface Props {
  title?: string;
}

const VideoPlayer: React.FC<Props> = ({ title = 'Course Video' }) => {
  return (
    <section className="card" style={{ height: '100%', padding: '0.5rem' }}>
      <div style={{ position: 'relative', width: '100%', paddingTop: '56.25%', borderRadius: '10px', overflow: 'hidden', background: '#000' }}>
        <div style={{ position: 'absolute', inset: 0, display: 'grid', placeItems: 'center', color: '#9CA3AF' }}>
          <span style={{ color: 'white', opacity: 0.9 }}>{title}</span>
        </div>
      </div>
      <div style={{ padding: '.5rem .25rem' }}>
        <small style={{ color: '#6B7280' }}>Video player placeholder</small>
      </div>
    </section>
  );
};

export default VideoPlayer;
