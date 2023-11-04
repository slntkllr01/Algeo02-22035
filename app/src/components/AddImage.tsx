// src/ImageSection.js
// import React, { useState } from 'react';

function AddImage() {
//   const [selectedOption, setSelectedOption] = useState('texture'); // Default to 'texture'

//   const handleOptionChange = (option) => {
//     setSelectedOption(option);
//   };

  return (
    <div className="flex flex-col md:flex-row justify-center items-center mt-4 p-4 space-y-4 md:space-y-0 md:space-x-4">
      {/* Left side */}
      <div className="w-full md:w-1/2">
        <button className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Insert Image
        </button>

        <div className="mt-4">
          <label className="mr-2">Toggle by:</label>
          <div className="inline-flex items-center">
            <input
              type="radio"
              id="colorOption"
              name="toggleOption"
              value="color"
            //   checked={selectedOption === 'color'}
            //   onChange={() => handleOptionChange('color')}
              className="mr-2"
            />
            <label htmlFor="colorOption" className="mr-4">Color</label>

            <input
              type="radio"
              id="textureOption"
              name="toggleOption"
              value="texture"
            //   checked={selectedOption === 'texture'}
            //   onChange={() => handleOptionChange('texture')}
            />
            <label htmlFor="textureOption">Texture</label>
          </div>
        </div>

        <button className="bg-blue-500 text-white py-2 px-4 rounded mt-4 hover:bg-blue-600">
          Search
        </button>
      </div>

      {/* Right side */}
      <div className="w-full md:w-1/2">
        {/* Display image area (you can add your display logic here) */}
        <div className="border border-gray-300 h-64 w-full bg-gray-100 rounded-lg">
          {/* Display images or other content here */}
        </div>
      </div>
    </div>
  );
}

export default AddImage;
