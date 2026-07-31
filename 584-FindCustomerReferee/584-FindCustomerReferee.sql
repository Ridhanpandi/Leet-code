-- Last updated: 31/07/2026, 08:54:17
# Write your MySQL query statement below
SELECT name 
FROM Customer
WHERE COALESCE(referee_id, 0) != 2;