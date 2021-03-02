-- Displays the average temperature (°F) by city ordered by temp DESC
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
