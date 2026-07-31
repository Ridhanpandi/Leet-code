-- Last updated: 31/07/2026, 08:54:12
# Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;