-- List all shows.
-- A script that script that lists all genres from hbtn_0d_tvshows 
-- and displays the number of shows linked to each
-- First column called genre, second column called number_of_shows
-- A genre that with no shows linked isn't displayed

SELECT name, COUNT(name) AS number_of_shows
   FROM ((tv_genres AS tg
	INNER JOIN tv_show_genres AS tsg
	ON tsg.genre_id=tg.id) 
		
	INNER JOIN tv_shows AS ts
	ON ts.id = tsg.show_id)
   WHERE show_id IS NOT NULL
   GROUP BY name
   ORDER BY number_of_shows DESC;
