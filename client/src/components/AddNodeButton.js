import React from 'react';
import './AddNodeButton.css';

const AddNodeButton = ({ onClick }) => {
  return (
    <button className="add-node-button" onClick={onClick}>
      Add Node
    </button>
  );
};

export default AddNodeButton;