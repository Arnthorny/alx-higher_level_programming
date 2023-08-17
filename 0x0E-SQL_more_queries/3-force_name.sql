-- Create a table
-- This line creates the table force_name on the mysql server
-- The name field can’t be null
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
