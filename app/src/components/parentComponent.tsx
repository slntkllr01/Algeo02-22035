import React, { useState, useEffect } from 'react';
import CardComponent from './pagination';
import { error } from 'console';
import axios from "axios"; 

function ParentComponent() {
  const [uploadedData, setUploadedData] = useState([]);
  const [searchResults, setSearchResults] = useState([]);
  const [compareType, setCompareType] = useState<string>('Texture');
  const [currentTime, setCurrentTime] = useState(null);

  const fetchData = async () => {
    
    try {
      
      const response = await axios.get('http://localhost:5000/process_and_compare?compareType='+compareType, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      if (response.status != 200) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.data;
      setUploadedData(data);
      setSearchResults(data);
    } catch (error: any) {
      console.error('Error fetching data:', error.message);
      // Tambahkan logika atau state untuk menangani error, misalnya menampilkan pesan kesalahan kepada pengguna
    }
  };

  useEffect(() => {
    // fetchData();
  }, []); // <-- Ditambahkan dependensi kosong untuk menjalankan useEffect hanya sekali pada saat mounting

  const handlePageChange = (page: number) => {
    const startIndex = (page - 1) * 8;
    const endIndex = startIndex + 8;
    setUploadedData(searchResults.slice(startIndex, endIndex));
  };

  const handleSearch = () => {
    // const now = new Date();
    // const formattedTime = now.toLocaleTimeString();
    // setCurrentTime(formattedTime);
    fetchData();
  };

  
  // const url='http://localhost:5000/'
  // const dataDummy = [
  //       {
  //           "file_path": "static/logo192.png",
  //           "similarity": 99.9371439304287
  //       },
  //       {
  //           "file_path":"uploaded_dataset\\black-and-white-ebony-60x60.jpg",
  //           "similarity": 72.53914757703008
  //       },
  //       {
  //           "file_path": "uploaded_dataset\\ambrosia-maple-gw-60x60.jpg",
  //           "similarity": 67.53526560397319
  //       },
  //       {
  //           "file_path": "uploaded_dataset\\black-cherry-100x100.jpg",
  //           "similarity": 61.41683916052517
  //       },
  //       {
  //           "file_path": "uploaded_dataset\\balsa-s-60x60.jpg",
  //           "similarity": 60.87699083278243
  //       },
  //       {
  //           "file_path": "uploaded_dataset\\black-cottonwood-44x60.jpg",
  //           "similarity": 60.63935510904452
  //       },
  //       {
  //           "file_path": "uploaded_dataset\\aspen-s-60x60.jpg",
  //           "similarity": 60.56859413551724
  //       },
  //       {
  //           "file_path": "uploaded_dataset\\amboyna-60x60.jpg",
  //           "similarity": 60.50439009053634
  //       },
  //       {
  //           "file_path": "uploaded_dataset\\atlantic-white-cedar-44x60.jpg",
  //           "similarity": 60.42915957318403
  //       },
  //       {
  //           "file_path": "uploaded_dataset\\balsam-fir-44x60.jpg",
  //           "similarity": 60.408500362080616
  //       },
  //       {
  //           "file_path": "uploaded_dataset\\balsam-poplar-jn-57x60.jpg",
  //           "similarity": 60.37264800871348
  //       },
  //       {
  //           "file_path": "uploaded_dataset\\black-ash-44x60.jpg",
  //           "similarity": 60.031732845413934
  //       }
  //   ]
  const handleCompareButtonClick = () => {
    setCompareType(compareType)

  };
  
  return (
    <div>
      <button
        className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-600"
        onClick={handleSearch}
      >
        Search
      </button>
      {currentTime && (
        <div>
          <h2>Current Time:</h2>
          <p>{currentTime}</p>
        </div>
      )}
      <CardComponent 
        data={uploadedData}
        totalItems={searchResults.length}
        onPageChange={handlePageChange}
      />
      <div className="flex flex-row gap-2 m-4 items-center">
          <label>
            Texture
          </label>

          <label htmlFor="check" className="bg-gray-300 cursor-pointer relative w-20 h-10 rounded-full">
            <input type="checkbox" id="check" className="sr-only peer" />
            <span className="w-2/5 h-4/5 bg-blue-500 absolute rounded-full left-1 top-1
            peer-checked:bg-blue-500 peer-checked:left-11 transition-all duration-500"></span>
          </label>

          <label>
            Color
            <input
              type="button"
              value="Compare"
              onClick={handleCompareButtonClick}
            />
          </label>
        </div>
    </div>
  );
}

export default ParentComponent;
