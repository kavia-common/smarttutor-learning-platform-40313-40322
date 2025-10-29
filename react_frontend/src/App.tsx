import React from 'react';
import { Routes } from 'react-router';
import { AppRoutes } from './routes';
import NavBar from './components/NavBar';

const App: React.FC = () => {
  return (
    <div className="app gradient-bg" style={{ minHeight: '100%' }}>
      <NavBar />
      <main className="container" style={{ paddingTop: '1rem', paddingBottom: '2rem' }}>
        <Routes>{AppRoutes}</Routes>
      </main>
    </div>
  );
};

export default App;
