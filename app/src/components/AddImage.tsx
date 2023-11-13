// import dummypic from "../assets/pic.png"
import React, {useState, useEffect} from "react";
import UploadImage from "./UploadImage";

function AddImage() {

  const [message, setMessage] = useState('test');
  useEffect(() => {
    fetch('http://localhost:5000/time')
      .then((res) => res.json())
      .then((data) => setMessage(data.time))
      .catch((error) => {
        console.error("Error fetching hello message:", error);
      });
  }, []);

  return (
    <div className="flex flex-row md:flex-col justify-evenly items-center mt-4 p-4 space-y-4 md:space-y-0 md:space-x-4">
      <div className="m-2">
        <p>Ini dari Backend {message}</p>
      </div>

      <div className="w-full md:w-1/2 flex flex-col justify-center items-center m-4">
        {/* Display image area (you can add your display logic here) */}
        <div className="border border-gray-300 h-64 w-64 bg-gray-100 rounded-lg flex items-center justify-center">
          <img src={require("../assets/pic.png")} alt="dummy"/>
          {/* Display images or other content here */}
        </div>
        <div>
          <p className="text-sm pt-2">dummy.jpg</p>
        </div>
      </div>

      <div className="m-4">
        <UploadImage />
      </div>

      <div className="m-4">
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
      </div>
      
      <div className="m-4">
        <button className="bg-blue-500 text-white py-2 px-4 m-4 rounded hover:bg-blue-600">
          Search
        </button>
      </div>
        
    </div>
  );
}

export default AddImage;
