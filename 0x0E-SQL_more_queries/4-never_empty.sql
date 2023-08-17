-- Create a table
-- This query creates the table id_not_null on the mysql server
-- The id field can’t be null and has a defaut value of 1
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
