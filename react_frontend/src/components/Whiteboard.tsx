import React, { useRef, useEffect } from 'react';

const Whiteboard: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const cvs = canvasRef.current;
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    if (!ctx) return;
    // Draw a faint grid to suggest whiteboard
    const w = cvs.width;
    const h = cvs.height;
    ctx.clearRect(0,0,w,h);
    ctx.fillStyle = '#fff';
    ctx.fillRect(0,0,w,h);
    ctx.strokeStyle = 'rgba(17,24,39,0.06)';
    for (let x=0; x<w; x+=24) {
      ctx.beginPath(); ctx.moveTo(x,0); ctx.lineTo(x,h); ctx.stroke();
    }
    for (let y=0; y<h; y+=24) {
      ctx.beginPath(); ctx.moveTo(0,y); ctx.lineTo(w,y); ctx.stroke();
    }
  }, []);

  return (
    <section className="card" style={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      <div style={{ padding: '.5rem .75rem', borderBottom: '1px solid rgba(17,24,39,.06)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <strong>Whiteboard</strong>
        <div style={{ display: 'flex', gap: '.5rem' }}>
          <button className="btn btn-ghost">Pen</button>
          <button className="btn btn-ghost">Erase</button>
          <button className="btn btn-ghost">Clear</button>
        </div>
      </div>
      <div style={{ flex: 1, padding: '.75rem' }}>
        <div style={{ width: '100%', height: '100%', borderRadius: '10px', overflow: 'hidden', border: '1px solid rgba(17,24,39,.06)' }}>
          <canvas ref={canvasRef} width={1600} height={900} style={{ width: '100%', height: '100%', display: 'block', background: '#ffffff' }} />
        </div>
      </div>
    </section>
  );
};

export default Whiteboard;
