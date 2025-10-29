import React from 'react';
import { Link } from 'react-router-dom';
import { useCourses } from '@api/hooks';

const placeholders = Array.from({ length: 6 }).map((_, i) => ({
  id: i + 1,
  title: `Course ${i + 1}`,
  desc: 'Learn effectively with SmartTutor.',
  badge: i % 2 ? 'Popular' : 'New'
}));

// PUBLIC_INTERFACE
const Catalog: React.FC = () => {
  const { items, loading, error } = useCourses(12);
  const hasLive = items && items.length > 0 && !error;

  const renderCard = (id: number, title: string, desc?: string, badgeText?: string) => (
    <div className="card" key={id} style={{ padding: '1rem', display: 'flex', gap: '1rem', alignItems: 'center' }}>
      <div style={{ width: 80, height: 80, borderRadius: 12, background: 'rgba(37,99,235,.08)', display: 'grid', placeItems: 'center', color: 'var(--color-primary)', fontWeight: 700 }}>
        {id}
      </div>
      <div style={{ flex: 1 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '.5rem' }}>
          <h3 style={{ margin: 0 }}>{title}</h3>
          <span style={{ fontSize: 12, background: 'rgba(245,158,11,.15)', color: 'var(--color-secondary)', padding: '.15rem .4rem', borderRadius: 6 }}>
            {badgeText || 'New'}
          </span>
        </div>
        <p style={{ marginTop: '.25rem', color: '#6B7280' }}>{desc || 'Learn effectively with SmartTutor.'}</p>
      </div>
      <Link to={`/course/${id}`} className="btn btn-primary">View</Link>
    </div>
  );

  return (
    <div className="container" style={{ display: 'grid', gridTemplateColumns: '1fr 320px', gap: '1rem' }}>
      <div style={{ display: 'grid', gap: '1rem' }}>
        {loading && placeholders.slice(0, 3).map((p) => renderCard(p.id, p.title, p.desc, p.badge))}
        {!loading && hasLive && items.map((c) => renderCard(c.id, c.title, c.description))}
        {!loading && !hasLive && placeholders.map((p) => renderCard(p.id, p.title, p.desc, p.badge))}
        {error && (
          <div className="card" style={{ padding: '1rem', color: '#B91C1C', background: 'rgba(239,68,68,0.06)' }}>
            Failed to load courses from backend. Showing placeholders. Error: {String(error)}
          </div>
        )}
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
