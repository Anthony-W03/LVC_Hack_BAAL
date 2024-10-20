import React, { useState } from 'react';
import './App.css';
import NavBar from './components/NavBar';
import NetworkViz from './components/NetworkViz';
import ColorLegend from './components/ColorLegend';
import AddNodeButton from './components/AddNodeButton';

function App() {
  const [data, setData] = useState({
    nodes: [
      { id: 'Node 1', group: 1 },
      { id: 'Node 2', group: 2 },
      { id: 'Node 3', group: 3 },
    ],
    links: [
      { source: 'Node 1', target: 'Node 2' },
      { source: 'Node 2', target: 'Node 3' },
    ],
  });

  const handleAddNode = () => {
    const newNodeId = `Node ${data.nodes.length + 1}`;
    const newNode = { id: newNodeId, group: Math.floor(Math.random() * 3) + 1 };
    setData(prevData => ({
      nodes: [...prevData.nodes, newNode],
      links: [...prevData.links, { source: prevData.nodes[prevData.nodes.length - 1].id, target: newNodeId }],
    }));
  };

  return (
    <div className="App">
      <NavBar title="Network Visualization" />
      <div className="main-content">
        <div className="viz-container">
          <NetworkViz data={data} />
        </div>
        <ColorLegend />
        <AddNodeButton onClick={handleAddNode} />
      </div>
    </div>
  );
}

export default App;