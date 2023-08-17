-- Create a table and a database

-- This query creates the database on the mysql server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- This query creates the table states on the mysql server in the hbtn_0d_usa database
-- The id field must be unique, can't be null, auto-generated and is a primary key
-- The state_id field must be unique, can't be null, auto-generated and is a foreign key
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL UNIQUE AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
