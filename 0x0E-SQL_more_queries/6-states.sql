-- Create a table and a database

-- This query creates the database on the mysql server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- This query creates the table states on the mysql server in the hbtn_0d_usa database
-- The id field must be unique, can't be null, auto-generated and is a primary key
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
