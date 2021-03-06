-- Script that lists all Comedy shows in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT tv_shows.title FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_genres.id = tv_show_genres.genre_id AND tv_show_genres.show_id = tv_shows.id AND tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
