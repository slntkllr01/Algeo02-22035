import React, { useState, useEffect } from 'react';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  pages: JSX.Element[];
  maxPages: number;
}

const Modal: React.FC<ModalProps> = ({ isOpen, onClose, title, pages, maxPages }) => {
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    // Reset currentPage to 1 when isOpen changes
    setCurrentPage(1);
  }, [isOpen]);

  const handleNextPage = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.stopPropagation();
    setCurrentPage((prevPage) => Math.min(maxPages, prevPage + 1));
  };

  const handlePrevPage = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.stopPropagation();
    setCurrentPage((prevPage) => Math.max(1, prevPage - 1));
  };

  return (
    <div className={`z-50 fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 ${isOpen ? 'block' : 'hidden'}`} onClick={onClose}>
      <div className="bg-white p-8 rounded-md w-3/4 h-3/4">
        <h2 className="text-2xl font-bold mb-4 text-center">{title}</h2>
        {pages[currentPage - 1]}
        <div className="flex justify-between mt-4">
          {currentPage > 1 && (
            <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={(e) => handlePrevPage(e)}>
              Sebelumnya
            </button>
          )}

          {currentPage < maxPages ? (
            <button className="bg-blue-500 text-white px-4 py-2 rounded ml-auto" onClick={(e) => handleNextPage(e)}>
              Selanjutnya
            </button>
          ) : (
            <button className="bg-red-500 text-white px-4 py-2 rounded" onClick={onClose}>
              Keluar
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

function Title() {
  const [conceptModalOpen, setConceptModalOpen] = useState(false);
  const [useModalOpen, setUseModalOpen] = useState(false);
  const [aboutUsModalOpen, setAboutUsModalOpen] = useState(false);

  const openConceptModal = () => {
    setConceptModalOpen(true);
  };

  const closeConceptModal = () => {
    setConceptModalOpen(false);
  };

  const openUseModal = () => {
    setUseModalOpen(true);
  };

  const closeUseModal = () => {
    setUseModalOpen(false);
  };

  const openAboutUsModal = () => {
    setAboutUsModalOpen(true);
  };

  const closeAboutUsModal = () => {
    setAboutUsModalOpen(false);
  };

  const conceptPages = [
    <div>
      <p> Program ini menggunakan skema temu balik gambar menggunakan Content-Based Image Retrieval baik dengan parameter warna maupun tekstur. Hal tersebut memanfaatkan konsep aljabar vektor.</p>
    </div>,
    <div>
      <h3>Contoh berdasarkan parameter warna</h3>
      <img src={require("../assets/concept-image1.jpg")} alt="Concept 1" className='lg:w-1/2'/>
    </div>,
    <div>
      <h3>Contoh berdasarkan parameter warna atau tekstur</h3>
      <img src={require("../assets/concept-image-2.jpg")} alt="Concept 1" className='lg:w-1/2'/>
    </div>,
  ];

  const usePages = [
    <div>
      <h3>Upload gambar yang ingin kamu bandingkan</h3> 
      <img src={require("../assets/use-image1.png")} alt="Use 1" />
      <p>Jika berhasil, akan muncul pesan dan gambarmu akan tertera di placeholder gambar.</p>
    </div>,
    <div>
      <h3>Upload dataset gambar</h3>
      <img src={require("../assets/use-image2.png")} alt="Use 2" />
      <p>Tekan tombol Choose File dan pilih gambar-gambar dari folder gambar yang kamu ingin bandingkan</p>
    </div>,
    <div>
      <h3>Pilih kamu ingin melakukan komparasi berdasarkan tekstur atau warna</h3>
      <img src={require("../assets/use-image3.png")} alt="Use 3" />
    </div>,
    <div>
      <p>Selanjutnya, klik tombol 'Search' dan kamu akan melihat hasil gambar-gambar dari datasetmu yang paling mirip</p>
    </div>,
  ];

  const aboutUsPages = [
    <div>
      <h3>We are Melati, Shulha, and El...</h3>
      <img src={require("../assets/about-us-image1.jpg")} alt="About Us 1" className='lg:w-1/2' />
    </div>,
    <div>
      <h3>We are struggling through this...</h3>
      <img src={require("../assets/about-us-image3.jpg")} alt="About Us 1" className='lg:w-1/2' />
    </div>,
    <div>
      <h3>We are doing our best...</h3>
      <img src={require("../assets/about-us-image2.jpg")} alt="About Us 1" className='lg:w-1/2'/>
    </div>,
  ];

  return (
    <div className="bg-gray-800 p-3 flex justify-between items-center">
      <div className="flex items-center">
        <span className="pl-4 text-3xl text-white mr-2">&#9733;</span>
        <span className="text-white font-bold">SangkuLens</span>
      </div>
      <nav>
        <ul className="flex space-x-10 text-white pr-8">
          <li>
          <button className="hover:text-gray-300 focus:outline-none" onClick={openConceptModal}>
              Concept
            </button>
          </li>
          <li>
            <button className="hover:text-gray-300 focus:outline-none" onClick={openUseModal}>
              How to Use
            </button>
          </li>
          <li>
            <button className="hover:text-gray-300 focus:outline-none" onClick={openAboutUsModal}>
              About Us
            </button>
          </li>
        </ul>
      </nav>

      {/* Modal untuk Concept */}
      <Modal isOpen={conceptModalOpen} onClose={closeConceptModal} title="Concept" pages={conceptPages} maxPages={4} />

      {/* Modal untuk Use */}
      <Modal isOpen={useModalOpen} onClose={closeUseModal} title="How to Use" pages={usePages} maxPages={4} />

      {/* Modal untuk About Us */}
      <Modal isOpen={aboutUsModalOpen} onClose={closeAboutUsModal} title="About Us" pages={aboutUsPages} maxPages={4} />
    </div>
  );
}

export default Title;
