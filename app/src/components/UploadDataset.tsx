import React, { useState } from 'react';
import axios from "axios"; 


const MultiFileUpload: React.FC = () => {
  const [uploadMessage, setUploadMessage] = useState<string>('');
  const [folderPath, setFolderPath] = useState<string>('');
  const [uploadedPaths, setUploadedPaths] = useState<string[]>([]); 

  const handleUpload = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const folderInput = document.getElementById('folderInput') as HTMLInputElement;
    const files = folderInput?.files;

    if (!files || files.length === 0) {
      setUploadMessage('Please select a folder.');
      return;
    }

    const formData = new FormData();

    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      formData.append('files[]', file, file.webkitRelativePath || '');

       // Simpan path ke dalam array
      setUploadedPaths(prevPaths => [...prevPaths, file.webkitRelativePath || '']);
    }

    try {
      const response = await axios.post('http://localhost:5000/upload_multidata', {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      if (response.status === 200) {
        const data = await response.data();
        setUploadMessage('Folder and its contents uploaded successfully.');
        setFolderPath(data.folder_path);
      } else {
        const data = await response.data();
        setUploadMessage(data.message || 'Upload failed.');
      }
    }
     catch (error) {
      console.error('Error during upload:', error);
      setUploadMessage('An error occurred during upload.');
    }
  };


  return (
    <div className="container mx-auto mt-8">
      <form onSubmit={handleUpload}>
        <label htmlFor="folderInput" className="block text-lg font-semibold mb-2">
          Select Folder to Upload:
        </label>
        <input
          type="file"
          id="folderInput"
          // @ts-ignore
          webkitdirectory
          directory
          multiple
          className="border p-2"
        />
        <button type="submit" className="mt-4 bg-blue-500 text-white p-2 rounded"
        >
          Upload
        </button>
        {uploadMessage && <p className="text-red-400 mt-2">{uploadMessage}</p>}
      </form>

      <form method="post" encType="multipart/form-data">
        <input type="file" name="files[]" multiple />
        <input type="submit" value="Upload" />
      </form>

    </div>
  );
};

export default MultiFileUpload;






// // DropzoneComponent.jsx

// import React, { useCallback } from 'react';
// import { useDropzone } from 'react-dropzone';
// import 'dropzone/dist/dropzone.css';

// interface DropzoneComponentProps {
//   onDrop: (acceptedFiles: File[]) => void;
// }

// const DropzoneComponent: React.FC<DropzoneComponentProps> = ({ onDrop }) => {
//   const { getRootProps, getInputProps } = useDropzone({
//     onDrop,
//     multiple: false, // Adjust as needed
//     // accept: null, // Allow any file type
//   });

//   return (
//     <div {...getRootProps()} className="dropzone">
//       <input {...getInputProps()} />
//       <p>Drag 'n' drop a folder here, or click to select a folder</p>
//     </div>
//   );
// };

// export default DropzoneComponent;

// import React, {useCallback} from 'react';
// import axios from 'axios';

// const WebDAVComponent = () => {
//   const handleUpload = useCallback(async () => {
//     try {
//       const serverUrl = 'http://localhost:5000/webdav'; // Replace with your WebDAV server URL
//       const username = 'your_username'; // Replace with your WebDAV username
//       const password = 'your_password'; // Replace with your WebDAV password
//       const folderPath = '/path/to/uploaded/folder'; // Replace with the desired path

//       const authHeader = `Basic ${btoa(`${username}:${password}`)}`;
//       const headers = {
//         Authorization: authHeader,
//         'Content-Type': 'application/octet-stream', // Adjust based on your needs
//       };

//       // Create the folder (MKCOL request)
//       await axios.request({
//         method: 'mkcol',
//         url: `${serverUrl}${folderPath}`,
//         headers,
//       });

//       console.log('Folder created successfully!');
//     } catch (error) {
//       console.error('Error creating folder:', error);
//     }
//   }, []);

//   return (
//     <div>
//       <button onClick={handleUpload}>Upload Folder</button>
//     </div>
//   );
// };

// export default WebDAVComponent;