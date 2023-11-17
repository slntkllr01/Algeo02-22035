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
      <h3>Title 1</h3>
      <img src="concept-image1.jpg" alt="Concept Image 1" />
      <p>Page 1 content...</p>
    </div>,
    // ... tambahkan halaman-halaman lain sesuai kebutuhan
  ];

  const usePages = [
    <div>
      <h3>Title 1</h3>
      <img src="use-image1.jpg" alt="Use Image 1" />
      <p>Page 1 content...</p>
    </div>,
    // ... tambahkan halaman-halaman lain sesuai kebutuhan
  ];

  const aboutUsPages = [
    <div>
      <h3>Title 1</h3>
      <img src="about-us-image1.jpg" alt="About Us Image 1" />
      <p>Page 1 content...</p>
    </div>,
    // ... tambahkan halaman-halaman lain sesuai kebutuhan
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
              Use
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
      <Modal isOpen={useModalOpen} onClose={closeUseModal} title="Use" pages={usePages} maxPages={4} />

      {/* Modal untuk About Us */}
      <Modal isOpen={aboutUsModalOpen} onClose={closeAboutUsModal} title="About Us" pages={aboutUsPages} maxPages={4} />
    </div>
  );
}

export default Title;
