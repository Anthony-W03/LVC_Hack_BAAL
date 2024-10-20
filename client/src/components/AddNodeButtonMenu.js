import React, { useState, useEffect } from 'react';
import { fetchConnectionMenu } from '../services/api'; // Import the function
import './AddNodeButtonMenu.css'; // We'll create this CSS file next

const AddNodeMenu = ({ onClose }) => {
  const [nodeType, setNodeType] = useState('');
  const [nodeName, setNodeName] = useState('');
  const [description, setDescription] = useState('');
  const [priority, setPriority] = useState('medium');
  const [dueDate, setDueDate] = useState('');
  const [menuOptions, setMenuOptions] = useState([]); // New state for menu options

  useEffect(() => {
    // Fetch menu options when component mounts
    const getMenuOptions = async () => {
      try {
        const options = await fetchConnectionMenu();
        setMenuOptions(options);
      } catch (error) {
        console.error('Error fetching menu options:', error);
      }
    };
    getMenuOptions();
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you would handle the node creation logic
    console.log('Creating node:', { 
      type: nodeType, 
      nodeName,
      description,
      priority,
      dueDate
    });
    onClose();
  };

  return (
    <div className="add-node-menu">
      <h3>Add New Node</h3>
      <form onSubmit={handleSubmit}>
        {/* Node Type */}
        <div className="form-group">
          <label htmlFor="nodeType">Node Type:</label>
          <select
            id="nodeType"
            value={nodeType}
            onChange={(e) => setNodeType(e.target.value)}
            required
          >
            <option value="">Select a type</option>
            {menuOptions.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </div>

        {/* Node Name */}
        <div className="form-group">
          <label htmlFor="nodeName">Node Name:</label>
          <input
            type="text"
            //id="nodeName"
            value={nodeName}
            onChange={(e) => setNodeName(e.target.value)}
            required
          />
        </div>

        {/* Description */}
        <div className="form-group">
          <label htmlFor="description">Description:</label>
          <input
            type="text"
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>

        {/* Priority */}
        <div className="form-group">
          <label htmlFor="priority">Priority:</label>
          <input
            type="text"
            id="priority"
            value={priority}
            onChange={(e) => setPriority(e.target.value)}
          />
        </div>

        {/* Due Date */}
        <div className="form-group">
          <label htmlFor="dueDate">Due Date:</label>
          <input
            type="text"
            id="dueDate"
            value={dueDate}
            onChange={(e) => setDueDate(e.target.value)}
          />
        </div>

        {/* Form Actions */}
        <div className="form-actions">
          <button type="submit">Create Node</button>
          <button type="button" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </div>
  );
};

export default AddNodeMenu;
