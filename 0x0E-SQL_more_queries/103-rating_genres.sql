-- List all shows.

-- A script that script that lists all shows,
--  from hbtn_0d_tvshows_rate by their rating.

SELECT name, SUM(tsr.rate) AS rating
    FROM ((tv_show_genres AS tsg
       INNER JOIN tv_genres AS tg
       ON tsg.genre_id=tg.id)

       INNER JOIN tv_show_ratings AS tsr
       ON tsr.show_id = tsg.show_id)
    GROUP BY name
    ORDER BY rating DESC;
