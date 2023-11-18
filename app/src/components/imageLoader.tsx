import React, { useState } from 'react';

const ProcessingImage = () => {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
  
    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files.length > 0) {
            setSelectedFile(event.target.files[0]);
          }
    };
  
    const handleUpload = async () => {
      if (!selectedFile) {
        alert('Please select a file');
        return;
      }
  
      const formData = new FormData();
      formData.append('file', selectedFile);
  
      try {
        const response = await fetch('http://localhost:5000/process_and_compare', {
          method: 'POST',
          body: formData,
        });
  
        if (response.ok) {
          const result = await response.json();
          alert(result.message);
        } else {
          alert('Error processing and comparing images');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    };
  
    return (
      <div>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload}>Process and Compare</button>
      </div>
    );
  };
  
  export default ProcessingImage;