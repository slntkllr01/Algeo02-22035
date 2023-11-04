import React, { useRef } from 'react';

function UploadDataset({ onUpload }) {
  const fileInputRef = useRef(null);

  const handleUpload = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  const handleFilesSelected = (event) => {
    const files = event.target.files;
    if (files.length > 0) {
      // You can process the selected files here
      onUpload(files);
    }
  };

  return (
    <div className="flex justify-center mt-4">
      <input
        type="file"
        accept=".jpg, .jpeg, .png"
        multiple
        style={{ display: 'none' }}
        ref={fileInputRef}
        onChange={handleFilesSelected}
      />
      <button
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        onClick={handleUpload}
      >
        Upload Dataset
      </button>
    </div>
  );
}

export default UploadDataset;