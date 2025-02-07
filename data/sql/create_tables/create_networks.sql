CREATE TABLE networks (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES useraccounts(id)
);