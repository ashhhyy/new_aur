import React, { useState, useEffect } from 'react';

const App: React.FC = () => {
  const [images, setImages] = useState<string[]>([]);
  const [isRunning, setIsRunning] = useState(false);

  const startRobot = async () => {
    try {
      const response = await fetch('/api/start', { method: 'POST' });
      if (response.ok) {
        setIsRunning(true);
      } else {
        alert('Failed to start the robot');
      }
    } catch (error) {
      alert('Error starting the robot');
    }
  };

  const stopRobot = async () => {
    try {
      const response = await fetch('/api/stop', { method: 'POST' });
      if (response.ok) {
        setIsRunning(false);
      } else {
        alert('Failed to stop the robot');
      }
    } catch (error) {
      alert('Error stopping the robot');
    }
  };

  const fetchImages = async () => {
    try {
      const response = await fetch('/api/camera/images');
      if (response.ok) {
        const data = await response.json();
        setImages(data.images || []);
      } else {
        alert('Failed to fetch images');
      }
    } catch (error) {
      alert('Error fetching images');
    }
  };

  useEffect(() => {
    fetchImages();
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif', backgroundColor: '#f0f8ff', color: '#333' }}>
      <h1 style={{ color: '#007acc' }}>Underwater Robot Dashboard</h1>
      <div style={{ marginBottom: '20px' }}>
        <button
          onClick={startRobot}
          disabled={isRunning}
          style={{
            marginRight: '10px',
            backgroundColor: isRunning ? '#a0a0a0' : '#28a745',
            color: 'white',
            border: 'none',
            padding: '10px 20px',
            cursor: isRunning ? 'not-allowed' : 'pointer',
            borderRadius: '5px',
          }}
        >
          Start
        </button>
        <button
          onClick={stopRobot}
          disabled={!isRunning}
          style={{
            backgroundColor: !isRunning ? '#a0a0a0' : '#dc3545',
            color: 'white',
            border: 'none',
            padding: '10px 20px',
            cursor: !isRunning ? 'not-allowed' : 'pointer',
            borderRadius: '5px',
          }}
        >
          Stop
        </button>
      </div>
      <h2 style={{ color: '#007acc' }}>Captured Images</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap' }}>
        {images.length === 0 && <p>No images available</p>}
        {images.map((imgUrl, index) => (
          <img
            key={index}
            src={imgUrl}
            alt={`Captured ${index}`}
            style={{ width: '200px', height: '150px', marginRight: '10px', marginBottom: '10px', objectFit: 'cover', borderRadius: '5px', border: '1px solid #ccc' }}
          />
        ))}
      </div>
      <button
        onClick={fetchImages}
        style={{
          marginTop: '10px',
          backgroundColor: '#007acc',
          color: 'white',
          border: 'none',
          padding: '10px 20px',
          cursor: 'pointer',
          borderRadius: '5px',
        }}
      >
        Refresh Images
      </button>
    </div>
  );
};

export default App;
