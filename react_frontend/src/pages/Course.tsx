import React from 'react';
import { useParams } from 'react-router-dom';
import VideoPlayer from '@components/VideoPlayer';
import Whiteboard from '@components/Whiteboard';
import Chat from '@components/Chat';

// PUBLIC_INTERFACE
const Course: React.FC = () => {
  const { id } = useParams();
  return (
    <div className="container" style={{ display: 'grid', gridTemplateColumns: 'minmax(280px, 1fr) minmax(420px, 1.2fr) minmax(280px, 1fr)', gap: '1rem', height: 'calc(100vh - 96px)' }}>
      <VideoPlayer title={`Course ${id} Video`} />
      <Whiteboard />
      <Chat />
    </div>
  );
};

export default Course;
