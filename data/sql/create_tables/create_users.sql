CREATE TABLE useraccounts (
    id INT PRIMARY KEY,
    username VARCHAR(255),
    fname VARCHAR(255),
    lname VARCHAR(255),
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255)
);