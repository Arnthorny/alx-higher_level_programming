-- List all shows.
-- A script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Displays NULL if a show doesn’t have a genre

SELECT title, genre_id
    FROM tv_shows AS ts
	LEFT JOIN tv_show_genres AS tsg
	ON ts.id=tsg.show_id
   ORDER BY title, genre_id;
