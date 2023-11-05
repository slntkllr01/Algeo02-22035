// src/App.js
import React from 'react';
import Title from './components/Title';
import AddImage from './components/AddImage'; // Import the ImageSection component
import Card from './components/Card';
import CardGrid from './components/CardGrid';

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Title />
      <AddImage />
      {/* <Card/> */}
      <CardGrid/>
    </div>
  );
}

export default App;
