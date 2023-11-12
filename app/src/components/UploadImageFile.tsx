import React, {useState, ChangeEvent} from "react";
import axios from "axios";  

const UploadImageFile: React.FC = () => {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);

    const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
      if (event.target.files && event.target.files.length>0) {
        setSelectedFile(event.target.files[0]);
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

        console.log('Error uploading dataset:', response.data);
      }
      catch(err){
        console.error(err);
      }
    };

    return(
        <div>
            <label htmlFor="uploadDataset">
                <input id="uploadDataset" name="file" type="file" onChange={handleFileChange}/>
            </label>
            <button className="bg-blue-500 text-white py-2 px-4 m-4 rounded hover:bg-blue-600"
            onClick={handleUpload}>
            Upload Image File
            </button>
        </div>
    );
};

export default UploadImageFile