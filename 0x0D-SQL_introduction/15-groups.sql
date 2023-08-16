-- List all rows
-- Group by records by score (top first)
SELECT score, COUNT(score) as number FROM second_table GROUP BY score
ORDER BY score DESC;
