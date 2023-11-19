import React, { HtmlHTMLAttributes, useState } from 'react';
import axios  from 'axios';
const MultiFileUpload = () => {
  const [uploadMessage, setUploadMessage] = useState('');

  const handleUploadMultipleFile = async (e: any) => {
    e.preventDefault();

    const folderInput = document.getElementById('folderInput') as HTMLInputElement;
    const files = folderInput?.files;

    if (!files || files.length === 0) {
      setUploadMessage('Please select a folder to upload.');
      return;
    }

    // You can perform additional validation or actions here before uploading.

    const formData = new FormData();

    for (let i = 0; i < files.length; i++) {
      formData.append('files[]', files[i]);
    }

    try {
      // Make your API call or upload logic here using formData
      // For example, using fetch:
      const response = await axios.post('http://localhost:5000/upload_multidata', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Handle the response as needed
      if (response.status == 200) {
        setUploadMessage('Upload successful!');
      } else {
        setUploadMessage('Upload failed. Please try again.');
      }
    } catch (error) {
      console.error('Error uploading files:', error);
      setUploadMessage('An error occurred during the upload. Please try again.');
    }
  };

  return (
    <form onSubmit={handleUploadMultipleFile} method="post" encType="multipart/form-data">
      <label htmlFor="folderInput" className="block text-lg font-semibold mb-2">
        Select Folder to Upload:
      </label>
      <input
        type="file"
        id="folderInput"
        // @ts-ignore
        webkitdirectory
        multiple
        className="border p-2"
      />
      <button type="submit" className="mt-4 bg-blue-500 text-white p-2 rounded">
        Upload
      </button>
      {uploadMessage && <p className="text-red-400 mt-2">{uploadMessage}</p>}
    </form>
  );
};

export default MultiFileUpload;
