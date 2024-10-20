import React from 'react';
import './NavBar.css';

const NavBar = ({ title }) => {
  return (
    <nav className="navbar">
      <div className="navbar-title">{title}</div>
      <div className="navbar-menu">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
      </div>
    </nav>
  );
};

export default NavBar;