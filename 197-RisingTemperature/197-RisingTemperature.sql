-- Last updated: 08/07/2026, 20:49:41
# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1
JOIN Weather w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;