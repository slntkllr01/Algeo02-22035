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


    const handleSearch = async () => {
      try {
        if (!selectedFile) {
          console.error("No file selected!");
          return;
        }
  
        const formData = new FormData();
        formData.append("file", selectedFile);
  
        const response = await axios.post('http://localhost:5000/process_and_compare', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
  
        // Menampilkan hasil perbandingan
        console.log('Image comparison result:', response.data);
      } catch (err) {
        console.error('Error processing and comparing images:', err);
      }
    };

    return (
    <div className="m-4">
      <label htmlFor="uploadImage" className="flex flex-col items-center">
        <div
          id="display_image"
          className="border border-gray-300 h-64 w-64 bg-gray-100 rounded-lg flex items-center justify-center"
          style={{
            backgroundImage: `url(${uploadImage})`,
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat',
            backgroundPosition: 'center',
          }}
        ></div>
        <div className="mt-8 items-center">
          <form>
          <input type="file" id="image" accept="image/png,image/jpg" onChange={handleFileChange} className="text-center" />
          <button
            className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-600"
            onClick={handleUpload} 
          >
            Insert Image
          </button>
          </form>
        </div>
      </label>
      {uploadMessage && <p className="text-red-400">{uploadMessage}</p>} 

      <div className="m-4 flex flex-col items-center">
          <button className="bg-blue-600 text-white py-2 px-4 m-4 rounded hover:bg-blue-600">
          <input
          type="file"
          id="fileInputControl"
          // @ts-ignore
          webkitdirectory
          multiple
        />
            Upload Dataset
          </button>

          <div className="flex flex-row gap-2 m-4 items-center">
          <label>
            Texture
          </label>

          <label htmlFor="check" className="bg-gray-300 cursor-pointer relative w-20 h-10 rounded-full">
            <input type="checkbox" id="check" className="sr-only peer" />
            <span className="w-2/5 h-4/5 bg-blue-300 absolute rounded-full left-1 top-1
            peer-checked:bg-blue-500 peer-checked:left-11 transition-all duration-500"></span>
          </label>

          <label>
            Color
          </label>
        </div>


        <div className="m-4 items-center justify-center">
          <button
            className="bg-blue-600 text-white py-2 px-4 m-4 rounded hover:bg-blue-600"
            onClick={handleSearch}
          >
            Search
          </button>
        </div>
      </div>
    </div>
    
    );
};

export default UploadDataset