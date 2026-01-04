CREATE DATABASE resume_db;
USE resume_db;

CREATE TABLE candidates (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    score INT
);

