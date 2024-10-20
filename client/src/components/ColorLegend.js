import React from 'react';
import './ColorLegend.css';

const ColorLegend = () => {
  const colors = [
    { name: 'You', color: '#70877F' },
    { name: 'Selected', color: '#EECF6D' },
    { name: 'Direct Connections', color: '#2F2963' },
    { name: 'Outer Connections', color: '#79779B' },
  ];

  return (
    <div className="color-legend">
      <h3>Color Legend</h3>
      {colors.map((item, index) => (
        <div key={index} className="legend-item">
          <div className="color-box" style={{ backgroundColor: item.color }}></div>
          <span>{item.name}</span>
        </div>
      ))}
    </div>
  );
};

export default ColorLegend;