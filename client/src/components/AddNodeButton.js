import React, { useState } from 'react';
import './AddNodeButton.css';
import AddNodeMenu from './AddNodeButtonMenu'; // We'll create this component next

const AddNodeButton = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <div className="add-node-container">
      <button className="add-node-button" onClick={toggleMenu}>
        Add Node
      </button>
      {isMenuOpen && <AddNodeMenu onClose={() => setIsMenuOpen(false)} />}
    </div>
  );
};

export default AddNodeButton;