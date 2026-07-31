-- Last updated: 31/07/2026, 08:53:25


select distinct author_id as id from Views
where author_id = viewer_id 
order by id;