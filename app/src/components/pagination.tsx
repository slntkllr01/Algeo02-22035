import React, { useState, useEffect } from 'react';
import axios from "axios"; 

interface CardComponentProps {
  data: Array<{ file_path: string; similarity: number }>;
  totalItems: number;
  onPageChange: (page: number) => void;
}


function CardComponent({data, totalItems, onPageChange}: CardComponentProps) {
  const [dataResult, setDataResult] = useState([]);
  interface CardData {
    file_path : string;
    similarity : number;
  }
  
  const convertStringToCardProps = (jsonString: string): Array<CardData> => {
    const data = JSON.parse(jsonString);
    return data.map(([file_path, similarity]: [string, number]) => ({
      title: `${similarity}%`,
      description: file_path,
    }));
  };
  
  const itemsPerPage = 8;
  const [currentPage, setCurrentPage] = useState(1);
  const indexLast = currentPage * itemsPerPage;
  const indexFirst = indexLast - itemsPerPage;
  const currentItems = dataResult.slice(indexFirst, indexLast)
  const totalPages = Math.ceil(dataResult.length / itemsPerPage);

  const handlePageChange = (page: number) => {
    // if (page >= 1 && page <= totalPages) {
      setCurrentPage(page);
    // }
  };

  const handleUpload = async () => {
    try{
      const response = await axios.get('http://localhost:5000/process_and_compare?compareType='+'Texture', {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setDataResult(response.data);
      console.log('log',response)
    }
    catch(err){
      console.error(err);
    }
  };
  
  // useEffect(() => {
  //   setCurrentPage(1);
  // }, [totalItems]);

  // const generatePageNumbers = () => {
  //   const pageNumbers = [];
  //   const maxPageNumbers = 9;

  //   if (totalPages <= maxPageNumbers) {
  //     for (let i = 1; i <= totalPages; i++) {
  //       pageNumbers.push(i);
  //     }
  //   } else {
  //     const half = Math.floor(maxPageNumbers / 2);
  //     let start = Math.max(currentPage - half, 1);
  //     let end = Math.min(start + maxPageNumbers - 1, totalPages);

  //     if (end - start + 1 < maxPageNumbers) {
  //       start = end - maxPageNumbers + 1;
  //     }

  //     if (start > 1) {
  //       pageNumbers.push(1);
  //       if (start > 2) {
  //         pageNumbers.push('...');
  //       }
  //     }

  //     for (let i = start; i <= end; i++) {
  //       pageNumbers.push(i);
  //     }

  //     if (end < totalPages) {
  //       if (end < totalPages - 1) {
  //         pageNumbers.push('...');
  //       }
  //       pageNumbers.push(totalPages);
  //     }
  //   }

  //   return pageNumbers;
  // };

  // const renderCards = () => {
  //   const startIndex = (currentPage - 1) * itemsPerPage;
  //   const endIndex = startIndex + itemsPerPage;
  //   const currentData = data.slice(startIndex, endIndex);
  
  //   return (
  //     <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
  //       {currentData.map((item, index) => (
  //         <div key={index} className="p-4 border rounded-lg shadow-lg w-[200px] h-[220px]">
  //           <div className="h-[83%]">
  //             {/* Bagian Atas: Foto atau gambar */}
  //             <div className="bg-blue-400 w-full h-full flex items-center justify-center">
  //               <span className="text-white text-xl font-bold">{item.file_path}</span>
  //             </div>
  //           </div>
  //           <div className="h-1/4 flex flex-col justify-center">
  //             {/* Bagian Bawah: Teks */}
  //             <h2 className="text-xl font-semibold text-center">{item.similarity}</h2>
  //           </div>
  //         </div>
  //       ))}
  //     </div>
  //   );
  // };

  return (
    <div>
      {/* {renderCards()} */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {currentItems.map((item: any, index: number) => (
          <div key={index} className="p-4 border rounded-lg shadow-lg w-[200px] h-[220px]">
            <div className="h-[83%]">
              {/* Bagian Atas: Foto atau gambar */}
              <div className="bg-blue-400 w-full h-full flex items-center justify-center">
                <img className="text-white text-xl font-bold" src={`http://localhost:5000/${item.file_path}`} />       
              </div>
              {/* Bagian Bawah: Teks */}
              <h2 className="text-xl font-semibold text-center">{item.similarity}</h2>
            </div>
          </div>
        ))}
      </div>
      {/* <button
        className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-600"
        onClick={handleUpload}
      >
        Search
      </button> */}
      <div className="flex justify-between mt-4">
        <button
          onClick={() => handlePageChange(currentPage - 1)}
          disabled={currentPage === 1}
          className="px-3 py-2 rounded-lg bg-gray-200"
        >
          Prev
        </button>
        {
          Array.from({length: totalPages}, (_,index)=> (
            <span
              key={index}
              className={`px-3 py-2 rounded-lg bg-gray-200 cursor-pointer`}
              onClick={() => handlePageChange(index + 1)}
            >
              {index + 1}
            </span>
          ))
        }
        {/* <div>
          {generatePageNumbers().map((page, index) => (
            <span
              key={index}
              className={`px-3 py-2 rounded-lg bg-gray-200 cursor-pointer ${
                page === currentPage ? 'bg-blue-500 text-white' : ''
              }`}
              onClick={() => {
                if (typeof page === 'number') {
                  handlePageChange(page);
                }
              }}
            >
              {page}
            </span>
          ))}
        </div> */}
        <button
          onClick={() => handlePageChange(currentPage + 1)}
          disabled={currentPage === totalPages}
          className="px-3 py-2 rounded-lg bg-gray-200"
        >
          Next
        </button>
      </div>
    </div>
  );
}

export default CardComponent;