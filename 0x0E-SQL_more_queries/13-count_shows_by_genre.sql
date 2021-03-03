-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Dont display a genre that doesnt have any shows linked
-- Results must be sorted in descending order by the number of shows linked
SELECT tv_genres.name AS "genre", COUNT(*) AS "number_of_shows"
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id = genre_id GROUP BY genre_id ORDER BY COUNT(*) DESC;
