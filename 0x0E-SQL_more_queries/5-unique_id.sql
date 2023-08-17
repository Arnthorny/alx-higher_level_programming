-- Create a table
-- This line creates the table unique_id on the mysql server
-- The id field must be unique and has a defaut value of 1
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
