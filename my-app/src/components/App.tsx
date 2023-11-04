// src/App.js
import React from 'react';
import Title from './Title';
import AddImage from './AddImage'; // Import the ImageSection component

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Title />
      <AddImage />
      <InfoSection numResults={resultImages.length} executionTime={0.57} />
      <ResultImages resultImages={resultImages} imagesPerPage={8} />
      <UploadDatasetButton onUpload={handleDatasetUpload} />
    </div>
  );
}

export default App;
