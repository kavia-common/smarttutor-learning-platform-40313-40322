import React, { useState } from 'react';

const Chat: React.FC = () => {
  const [messages, setMessages] = useState<string[]>([
    'Welcome to SmartTutor chat!',
    'Ask your questions here.'
  ]);
  const [text, setText] = useState('');

  const send = () => {
    if (!text.trim()) return;
    setMessages((m) => [...m, text.trim()]);
    setText('');
  };

  return (
    <aside className="card" style={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      <div style={{ padding: '.5rem .75rem', borderBottom: '1px solid rgba(17,24,39,.06)' }}>
        <strong>Chat</strong>
      </div>
      <div style={{ flex: 1, overflow: 'auto', padding: '.75rem', display: 'flex', flexDirection: 'column', gap: '.5rem' }}>
        {messages.map((m, i) => (
          <div key={i} style={{ alignSelf: i % 2 ? 'flex-end' : 'flex-start', maxWidth: '85%' }}>
            <div style={{
              background: i % 2 ? 'var(--color-primary)' : 'rgba(37,99,235,0.08)',
              color: i % 2 ? 'white' : 'inherit',
              padding: '.5rem .75rem', borderRadius: '10px'
            }}>{m}</div>
          </div>
        ))}
      </div>
      <div style={{ padding: '.5rem .75rem', borderTop: '1px solid rgba(17,24,39,.06)', display: 'flex', gap: '.5rem' }}>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Type a message"
          style={{ flex: 1, borderRadius: 10, border: '1px solid rgba(17,24,39,.12)', padding: '.55rem .75rem' }}
        />
        <button className="btn btn-primary" onClick={send}>Send</button>
      </div>
    </aside>
  );
};

export default Chat;
