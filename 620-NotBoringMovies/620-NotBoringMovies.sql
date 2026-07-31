-- Last updated: 31/07/2026, 08:53:56
# Write your MySQL query statement below

SELECT *
FROM cinema c
WHERE c.id % 2 =1 
    AND 
    c.description != 'boring'
ORDER BY c.rating DESC;