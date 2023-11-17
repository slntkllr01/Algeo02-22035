// src/App.js
import React from 'react';
import Title from './components/Title';
import AddImage from './components/AddImage'; // Import the ImageSection component

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Title />
      <AddImage />
    </div>
  );
}

export default App;
