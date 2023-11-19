// src/App.tsx
import React, { useEffect, useState } from 'react';
import Title from './components/Title';
import AddImage from './components/AddImage';
import CardComponent from './components/pagination';
import ParentComponent from './components/parentComponent';
import MultiFileUpload from './components/MultiFileUpload';

function App() {
  const date= new Date()
  // const [processedCardData, setProcessedCardData] = useState([]);

  // const fetchData = async () => {
  //   try {
  //     const response = await fetch('http://localhost:5000/process_and_compare');
  //     const data = await response.json();
  //     setProcessedCardData(data);
  //   } catch (error) {
  //     console.error('Error fetching data:', error);
  //   }
  // };

  // useEffect(() => {
  //   fetchData();
  // }, []);
  return (
    <div className="min-h-screen bg-blue-100 items-center">
      <Title />
      <div className="flex flex-row items-center justify-center">
        {/* <CardComponent data={processedCardData} /> */}
        <div className='flex flex-col items-center justify-center '>
          <AddImage />
          <MultiFileUpload/>
        </div >
        
        <ParentComponent/>
      </div>
      <div>
        {/* <CardComponent data={dataDummy}/> */}
      </div>
    </div>
  );
}

export default App;
