import React, { useState } from 'react';
import './AddNodeButtonMenu.css'; // We'll create this CSS file next

const AddNodeMenu = ({ onClose }) => {
  const [nodeType, setNodeType] = useState('');
  const [nodeName, setNodeName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you would handle the node creation logic
    console.log('Creating node:', { type: nodeType, name: nodeName });
    onClose();
  };

  return (
    <div className="add-node-menu">
      <h3>Add New Node</h3>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="nodeType">Node Type:</label>
          <select
            id="nodeType"
            value={nodeType}
            onChange={(e) => setNodeType(e.target.value)}
            required
          >
            <option value="">Select a type</option>
            <option value="type1">Type 1</option>
            <option value="type2">Type 2</option>
            <option value="type3">Type 3</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="nodeName">Node Name:</label>
          <input
            type="text"
            id="nodeName"
            value={nodeName}
            onChange={(e) => setNodeName(e.target.value)}
            required
          />
        </div>
        <div className="form-actions">
          <button type="submit">Create Node</button>
          <button type="button" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </div>
  );
};

export default AddNodeMenu;