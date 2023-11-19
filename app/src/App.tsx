// src/App.js
import React, { useState, useEffect } from 'react';
import Title from './components/Title';
import AddImage from './components/AddImage';
import CardComponent from './components/pagination';

function App() {

  const [CardData, setCardData] = useState([]);

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:5000/process_and_compare');
      const data = await response.json();
      setCardData(data)
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const cardData = [
    {"percentage": '70', "imgpath": "image1.jpg"},
    {"percentage": '85', "imgpath": "image2.jpg"},
    {"percentage": '60', "imgpath": "image3.jpg"},
    {"percentage": '70', "imgpath": "image1.jpg"},
    {"percentage": '85', "imgpath": "image2.jpg"},
    {"percentage": '60', "imgpath": "image3.jpg"},
    {"percentage": '70', "imgpath": "image1.jpg"},
    {"percentage": '85', "imgpath": "image2.jpg"},
    {"percentage": '60', "imgpath": "image3.jpg"},
    {"percentage": '70', "imgpath": "image1.jpg"},
    {"percentage": '85', "imgpath": "image2.jpg"},
    {"percentage": '60', "imgpath": "image3.jpg"},
  ]

  useEffect(() => {
    fetchData(); // Panggil fetchData ketika komponen di-mount
  }, []); // Parameter kedua berupa array kosong agar useEffect hanya dijalankan sekali saat komponen di-mount


  return (
    <div className="min-h-screen bg-blue-100">
      <Title />
      <div className="flex flex-row">
        <AddImage />
        <CardComponent data={cardData} />
      </div>
    </div>
  );
}

export default App;
