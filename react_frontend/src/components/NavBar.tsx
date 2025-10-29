import React from 'react';
import { Link, NavLink } from 'react-router-dom';

const NavBar: React.FC = () => {
  return (
    <header className="nav">
      <div className="container" style={{ display: 'flex', alignItems: 'center', gap: '1rem', padding: '.75rem 0' }}>
        <Link to="/" style={{ display: 'inline-flex', alignItems: 'center', gap: '.6rem' }}>
          <div style={{
            width: 36, height: 36, borderRadius: 10, background: 'var(--color-primary)',
            color: 'white', display: 'grid', placeItems: 'center', fontWeight: 800
          }}>S</div>
          <span style={{ fontWeight: 700, fontSize: '1.05rem' }}>SmartTutor</span>
        </Link>

        <nav style={{ marginLeft: 'auto', display: 'flex', gap: '.75rem' }}>
          <NavLink to="/catalog" className="btn btn-ghost">Catalog</NavLink>
          <NavLink to="/login" className="btn btn-primary">Login</NavLink>
        </nav>
      </div>
    </header>
  );
};

export default NavBar;
