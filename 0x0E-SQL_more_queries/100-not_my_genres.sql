-- List all shows.
-- A script that script that lists all comedy of the database. 

SELECT title, name
   FROM ((tv_shows AS ts 
	LEFT JOIN tv_show_genres AS tsg 
	ON ts.id=tsg.show_id)

	LEFT JOIN tv_genres as tg 
	ON tg.id=tsg.genre_id)
  ORDER BY title, name;
