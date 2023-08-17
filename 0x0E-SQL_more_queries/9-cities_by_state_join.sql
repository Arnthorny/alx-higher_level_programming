-- List all cities.
-- This query lists all the cities of California that can be found in the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
SELECT cities.id AS id, cities.name AS name, states.name AS name
    FROM cities, states 
   WHERE states.id=cities.state_id
   ORDER BY id;
