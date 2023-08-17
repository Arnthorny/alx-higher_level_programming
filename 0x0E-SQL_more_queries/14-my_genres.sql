-- List all shows.
-- A script that script that lists all genres of the show Dexter. 

SELECT name
    FROM ((tv_genres AS tg
	 INNER JOIN tv_show_genres AS tsg
	 ON tsg.genre_id=tg.id)

	 INNER JOIN tv_shows AS ts ON ts.id = tsg.show_id)
   WHERE title = 'Dexter'
   ORDER BY name;
