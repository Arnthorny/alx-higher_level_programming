-- Create a table

-- This line creates a table second_table in a mysql database
CREATE TABLE IF NOT EXISTS second_table (
        id INT,
        name VARCHAR(256),
        score INT
);

-- This line inserts a record in the table second_table
INSERT INTO second_table(id, name, score) VALUES(1, 'John', 10);
INSERT INTO second_table(id, name, score) VALUES(2, 'Alex', 3);
INSERT INTO second_table(id, name, score) VALUES(3, 'Bob', 14);
INSERT INTO second_table(id, name, score) VALUES(4, 'George', 8);
