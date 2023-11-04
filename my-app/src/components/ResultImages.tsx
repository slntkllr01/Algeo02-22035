// src/InfoSection.js
import React from 'react';

// src/ResultImages.js
import React, { useState, useEffect } from 'react';

function ResultImages({ resultImages, imagesPerPage }) {
  const [currentPage, setCurrentPage] = useState(1);
  const [displayedImages, setDisplayedImages] = useState([]);

  useEffect(() => {
    const startIndex = (currentPage - 1) * imagesPerPage;
    const endIndex = startIndex + imagesPerPage;
    const imagesToDisplay = resultImages.slice(startIndex, endIndex);
    setDisplayedImages(imagesToDisplay);
  }, [currentPage, resultImages, imagesPerPage]);

  const handlePageChange = (newPage) => {
    setCurrentPage(newPage);
  };

  return (
    <div>
      {/* Display images here */}
      {displayedImages.map((image, index) => (
        <div key={index} className="p-2 inline-block">
          <img src={image.url} alt={`Image ${index + 1}`} className="max-w-full h-auto" />
        </div>
      )}

      {/* Pagination buttons */}
      <div className="flex justify-center mt-4">
        {Array.from({ length: Math.ceil(resultImages.length / imagesPerPage) }, (_, index) => (
          <button
            key={index}
            className={`mx-2 px-3 py-2 rounded ${currentPage === index + 1 ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
            onClick={() => handlePageChange(index + 1)}
          >
            {index + 1}
          </button>
        )}
      </div>
    </div>
  );
}

export default ResultImages;

