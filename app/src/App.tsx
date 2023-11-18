// src/App.js
import React from 'react';
import Title from './components/Title';
import AddImage from './components/AddImage'; // Import the ImageSection component
import ProcessingImage from './components/imageLoader';
import MultiFileUpload from './components/UploadDataset';
import CardComponent from './components/pagination'

function App() {
  const data = [
    { title: 'Item 1', description: 'Description 1' },
    { title: 'Item 2', description: 'Description 2' },
    { title: 'Item 2', description: 'Description 2' },
    { title: 'Item 2', description: 'Description 2' },
    { title: 'Item 2', description: 'Description 2' },
    { title: 'Item 2', description: 'Description 2' },
    { title: 'Item 2', description: 'Description 2' },
    { title: 'Item 2', description: 'Description 2' },
    { title: 'Item 2', description: 'Description 2' },
    { title: 'Item 2', description: 'Description 2' },
    { title: 'Item 2', description: 'Description 2' },
        { title: 'Item 2', description: 'Description 2' },
    
  ];

  
  return (
    <div className="m-8 min-h-screen bg-blue-100">
      <Title />
      <div className="flex flex-row">
      <AddImage />
      {/* <CardComponent data = {data} /> */}
      {/* <CardComponent/> */}
      <MultiFileUpload/>
      </div>
    </div>
  );
}

export default App;
