import React, {useState, ChangeEvent} from "react";
import axios from "axios";  

const UploadDataset: React.FC = () => {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [uploadMessage, setUploadMessage] = useState<string | null>(null);
    const [uploadImage, setUploadImage] = useState<string | null>(null);

    const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
      const reader = new FileReader();
      if (event.target.files && event.target.files.length>0) {
        const file = event.target.files[0];
        setSelectedFile(file);
        reader.onloadend = () => {
          setUploadImage(reader.result as string);
          const displayImage = document.querySelector("#display_image") as HTMLDivElement;
          displayImage.style.backgroundImage = `url(${reader.result})`;
        }
        

        reader.readAsDataURL(file);
        // setSelectedFile(event.target.files[0]);
      }

    };


    const handleUpload = async () => {
      try{
        if(!selectedFile) {
          console.error("No file selected!");
          return;
        }
        console.log('Uploading file:', selectedFile);

        const formData = new FormData();
        formData.append("file", selectedFile);

        console.log('Form Data:', formData);

        const response = await axios.post('http://localhost:5000/upload_dataset', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        // tampilkan pesan
        setUploadMessage(`File "${selectedFile.name}" uploaded successfully!`);
        console.log('Error uploading dataset:', response.data);
      }
      catch(err){
        console.error(err);
      }
    };

    return(
      <div className="m-4 items-center">
        <label htmlFor="uploadImage">
          <div id="display_image"  className="border border-gray-300 h-64 w-64 bg-gray-100 rounded-lg flex items-center justify-center" style={{ backgroundImage: `url(${uploadImage})` }}></div>
          <input type="file" id="image" accept="image/png,image/jpg" onChange={handleFileChange} className="mt-4 p-4 text-center" />
        </label>
        <button
          className="bg-blue-500 text-white py-2 px-4 m-4 rounded hover:bg-blue-600"
          onClick={handleUpload} 
        >
          Insert Image
        </button>
        {uploadMessage && <p className="text-red-400">{uploadMessage}</p>} 
      </div>
    );
};

export default UploadDataset