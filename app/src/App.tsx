// src/App.js
import React from 'react';
import Title from './components/Title';
import AddImage from './components/AddImage'; // Import the ImageSection component
import ProcessingImage from './components/imageLoader';
import MultiFileUpload from './components/UploadDataset';

function App() {
  return (
    <div className="min-h-screen bg-blue-100">
      <Title />
      <AddImage />
      <MultiFileUpload/>
    </div>
  );
}

export default App;
