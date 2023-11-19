import React, { useState, useEffect } from 'react';
import CardComponent from './pagination_v2';
import { error } from 'console';

function ParentComponent() {
  const [uploadedData, setUploadedData] = useState([]);
  const [searchResults, setSearchResults] = useState([]);

  const fetchData = async () => {
    
    try {
      const response = await fetch('http://localhost:5000/process_and_compare');
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setUploadedData(data);
      setSearchResults(data);
    } catch (error: any) {
      console.error('Error fetching data:', error.message);
      // Tambahkan logika atau state untuk menangani error, misalnya menampilkan pesan kesalahan kepada pengguna
    }
  };

  useEffect(() => {
    fetchData();
  }, []); // <-- Ditambahkan dependensi kosong untuk menjalankan useEffect hanya sekali pada saat mounting

  const handlePageChange = (page: number) => {
    const startIndex = (page - 1) * 8;
    const endIndex = startIndex + 8;
    setUploadedData(searchResults.slice(startIndex, endIndex));
  };

  const handleSearch = () => {
    fetchData();
  };

  return (
    <div>
      <button
        className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-600"
        onClick={handleSearch}
      >
        Search
      </button>
      <CardComponent
        data={uploadedData}
        totalItems={searchResults.length}
        onPageChange={handlePageChange}
      />
    </div>
  );
}

export default ParentComponent;
