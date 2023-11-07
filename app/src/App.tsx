import React from 'react';
import CardComponent from './components/pagination';

function App() {
  // Contoh data yang akan Anda berikan ke CardComponent
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
    <div className="gap-10 min-h-screen bg-gray-100 flex flex-col items-center">
      <div className="text-transparent bg-clip-text bg-gradient-to-r from-blue-500 to-purple-600 font-bold text-3xl mt-10">
        SangkuLens - Reverse Image Search
      </div>
      <CardComponent data={data} /> {/* Kirim data sebagai properti */}
    </div>
  );
}

export default App;
