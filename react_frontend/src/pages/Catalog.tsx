import React from 'react';
import { Link } from 'react-router-dom';

const courses = Array.from({ length: 6 }).map((_, i) => ({
  id: i + 1,
  title: `Course ${i + 1}`,
  desc: 'Learn effectively with SmartTutor.',
  badge: i % 2 ? 'Popular' : 'New'
}));

// PUBLIC_INTERFACE
const Catalog: React.FC = () => {
  return (
    <div className="container" style={{ display: 'grid', gridTemplateColumns: '1fr 320px', gap: '1rem' }}>
      <div style={{ display: 'grid', gap: '1rem' }}>
        {courses.map((c) => (
          <div className="card" key={c.id} style={{ padding: '1rem', display: 'flex', gap: '1rem', alignItems: 'center' }}>
            <div style={{ width: 80, height: 80, borderRadius: 12, background: 'rgba(37,99,235,.08)', display: 'grid', placeItems: 'center', color: 'var(--color-primary)', fontWeight: 700 }}>
              {c.id}
            </div>
            <div style={{ flex: 1 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '.5rem' }}>
                <h3 style={{ margin: 0 }}>{c.title}</h3>
                <span style={{ fontSize: 12, background: 'rgba(245,158,11,.15)', color: 'var(--color-secondary)', padding: '.15rem .4rem', borderRadius: 6 }}>{c.badge}</span>
              </div>
              <p style={{ marginTop: '.25rem', color: '#6B7280' }}>{c.desc}</p>
            </div>
            <Link to={`/course/${c.id}`} className="btn btn-primary">View</Link>
          </div>
        ))}
      </div>

      <aside className="card" style={{ padding: '1rem', height: 'fit-content', position: 'sticky', top: '84px' }}>
        <h3 style={{ marginTop: 0 }}>AI Recommendations</h3>
        <p style={{ color: '#6B7280' }}>Personalized picks will appear here based on your activity.</p>
        <ul style={{ paddingLeft: '1rem', marginTop: '.5rem' }}>
          <li>Focus: Algebra Basics</li>
          <li>Recommended: Calculus I</li>
          <li>Next: Linear Algebra Essentials</li>
        </ul>
      </aside>
    </div>
  );
};

export default Catalog;
