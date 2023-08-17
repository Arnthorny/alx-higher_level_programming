-- List all shows.

-- A script that script that lists all shows,
--  from hbtn_0d_tvshows_rate by their rating.

SELECT title, SUM(rate) AS rating
    FROM (tv_show_ratings AS tsr
	  INNER JOIN tv_shows AS ts
	  ON tsr.show_id=ts.id)
   GROUP BY title
   ORDER BY rating DESC;
