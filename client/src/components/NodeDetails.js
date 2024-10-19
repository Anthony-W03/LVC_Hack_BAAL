import React from 'react';

const NodeDetails = ({ node }) => {
  if (!node) return null;

  return (
    <div>
      <h2>Selected Node: {node.name}</h2>
      <p>Connections: {node.connections.join(', ')}</p>
      <p>Type: {node.properties.type}</p>
      <p>Weight: {node.properties.weight}</p>
    </div>
  );
};

export default NodeDetails;