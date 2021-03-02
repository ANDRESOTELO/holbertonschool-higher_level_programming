-- Lists the number of records with the same score in a table
-- The result output display score and number of records
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY score DESC;
