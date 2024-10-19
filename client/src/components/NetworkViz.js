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

  return (
    <ForceGraph2D
      graphData={data}
      nodeLabel="name"
      nodeAutoColorBy="id"
      onNodeClick={(node) => {
        alert(`Clicked on ${node.name}`);
      }}
    />
  );
};

export default NetworkGraph;