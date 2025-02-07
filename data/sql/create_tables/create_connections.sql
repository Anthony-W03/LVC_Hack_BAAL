CREATE TABLE connections (
    id INT PRIMARY KEY,
    user_id INT,
    network_id INT,
    fname VARCHAR(255),
    lname VARCHAR(255),
    connection_through INT,
    linkedin VARCHAR(255),
    website VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    address VARCHAR(255),
    employment VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES useraccounts(id),
    FOREIGN KEY (network_id) REFERENCES networks(id)
);