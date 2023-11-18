import React, { useState } from 'react';

interface CardComponentProps {
  data: Array<{ percentage: string; imgpath: string }>;
}


function CardComponent({ data }: CardComponentProps) {

  interface CardData {
    percentage: number;
    imgpath: string;
  }
  
  const convertStringToCardProps = (jsonString: string): Array<CardData> => {
    const data = JSON.parse(jsonString);
    return data.map(([percentage, path]: [number, string]) => ({
      title: `${percentage}%`,
      description: path,
    }));
  };
  
  const itemsPerPage = 8;
  const [currentPage, setCurrentPage] = useState(1);

  const totalPages = Math.ceil(data.length / itemsPerPage);

  const handlePageChange = (page: number) => {
    if (page >= 1 && page <= totalPages) {
      setCurrentPage(page);
    }
  };

  const generatePageNumbers = () => {
    const pageNumbers = [];
    const maxPageNumbers = 9;

    if (totalPages <= maxPageNumbers) {
      for (let i = 1; i <= totalPages; i++) {
        pageNumbers.push(i);
      }
    } else {
      const half = Math.floor(maxPageNumbers / 2);
      let start = Math.max(currentPage - half, 1);
      let end = Math.min(start + maxPageNumbers - 1, totalPages);

      if (end - start + 1 < maxPageNumbers) {
        start = end - maxPageNumbers + 1;
      }

      if (start > 1) {
        pageNumbers.push(1);
        if (start > 2) {
          pageNumbers.push('...');
        }
      }

      for (let i = start; i <= end; i++) {
        pageNumbers.push(i);
      }

      if (end < totalPages) {
        if (end < totalPages - 1) {
          pageNumbers.push('...');
        }
        pageNumbers.push(totalPages);
      }
    }

    return pageNumbers;
  };

  const renderCards = () => {
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const currentData = data.slice(startIndex, endIndex);
  
    return (
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {currentData.map((item, index) => (
          <div key={index} className="p-4 border rounded-lg shadow-lg w-[200px] h-[220px]">
            <div className="h-[83%]">
              {/* Bagian Atas: Foto atau gambar */}
              <div className="bg-blue-400 w-full h-full flex items-center justify-center">
                <span className="text-white text-xl font-bold">{item.percentage}</span>
              </div>
            </div>
            <div className="h-1/4 flex flex-col justify-center">
              {/* Bagian Bawah: Teks */}
              <h2 className="text-xl font-semibold text-center">{item.imgpath}</h2>
            </div>
          </div>
        ))}
      </div>
    );
  };

  return (
    <div>
      {renderCards()}
      <div className="flex justify-between mt-4">
        <button
          onClick={() => handlePageChange(currentPage - 1)}
          disabled={currentPage === 1}
          className="px-3 py-2 rounded-lg bg-gray-200"
        >
          Prev
        </button>
        <div>
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
        </div>
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