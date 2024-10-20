import React from 'react';
import { ForceGraph2D } from 'react-force-graph';

const NetworkGraph = () => {
  const data = {
    nodes: [
      { id: 'You', name: 'You' },
      { id: 'Alice', name: 'Alice' },
      { id: 'Bob', name: 'Bob' },
      { id: 'Charlie', name: 'Charlie' },
    ],
    links: [
      { source: 'You', target: 'Alice' },
      { source: 'You', target: 'Bob' },
      { source: 'Alice', target: 'Charlie' },
    ]
  };

  const getNodeColor = (node) => {
    if (node.id === 'You') {
      return '#70877F';
    }
    const isConnectedToYou = data.links.some(
      link => link.source === 'You' && link.target === node.id
    );
    return isConnectedToYou ? '#2F2963' : '#79779B';
  };

  return (
    <ForceGraph2D
      graphData={data}
      nodeLabel="name"
      nodeColor={getNodeColor}
      onNodeClick={(node) => {
        node.nodeColor = '#EECF6D'; //fix
        alert(`Clicked on ${node.name}`);
      }}
    />
  );
};

export default NetworkGraph;