import React, { useState, useEffect } from 'react';
import { ForceGraph2D } from 'react-force-graph';
import { fetchNetwork } from '../services/api';

// const NetworkGraph = () => {
//     const data = {
//       nodes: [
//         { id: 'You', name: 'You' },
//         { id: 'Alice', name: 'Alice' },
//         { id: 'Bob', name: 'Bob' },
//         { id: 'Charlie', name: 'Charlie' },
//       ],
//       links: [
//         { source: 'You', target: 'Alice' },
//         { source: 'You', target: 'Bob' },
//         { source: 'Alice', target: 'Charlie' },
//       ]
//     };

function NetworkViz() {
  const [data, setData] = useState({
    nodes: [],
    links: []
  });
  const [highlightedNode, setHighlightedNode] = useState(null);

  useEffect(() => {
    fetchNetworkData();
  }, []);

  const fetchNetworkData = async () => {
    try {
      const userID = 1;
      const networkID = 1;

      const response = await fetchNetwork(userID, networkID);
      if (response.data) {
        setData(response.data);
      } else {
        console.error('Failed to fetch network data');
      }
    } catch (error) {
      console.error('Error fetching network data:', error);
    }
  };

  const getNodeColor = (node) => {
    if (node.id === highlightedNode) {
        return '#EECF6D';
      }
    if (node.id === 'You') {
      return '#70877F';
    }
    const isConnectedToYou = data.links.some(
      link => link.source === 'You' && link.target === node.id
    );
    return isConnectedToYou ? '#2F2963' : '#79779B';
  };

  const getInitials = (name) => {
    return name.split(' ').map(word => word[0]).join('').toUpperCase();
  };

  return (
    <ForceGraph2D
      graphData={data}
      nodeLabel="name"
      nodeColor={getNodeColor}
      nodeVal={10}
      linkWidth={2}
      onNodeClick={(node) => {
        setHighlightedNode(node.id);
      }}
      nodeCanvasObject={(node, ctx, globalScale) => {
        const nodeColor = getNodeColor(node);
        ctx.beginPath();
        ctx.arc(node.x, node.y, 5, 0, 2 * Math.PI, false);
        ctx.fillStyle = nodeColor;
        ctx.fill();

        const label = getInitials(node.name);
        const fontSize = 12/globalScale;
        ctx.font = `${fontSize}px Sans-Serif`;
        ctx.textAlign = 'center'
        ctx.textBaseline = 'middle'
        ctx.fillStyle = 'white' 
        ctx.fillText(label, node.x, node.y);
      }}
    />
  );
}

export default NetworkViz;
//export default NetworkGraph;
