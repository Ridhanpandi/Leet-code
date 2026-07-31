-- Last updated: 31/07/2026, 08:54:10
# Write your MySQL query statement below
select Class
from Courses group by Class having count(student)>=5;