-- List all shows.
-- This query lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- Results must be sorted in ascending order by tv_shows.title and tv_shows_genres.genre_id 
SELECT title, genre_id
    FROM tv_shows AS ts, tv_show_genres AS tsg
   WHERE ts.id=tsg.show_id 
   ORDER BY title, genre_id;
