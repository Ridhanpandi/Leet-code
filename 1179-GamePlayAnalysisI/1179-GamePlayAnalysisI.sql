-- Last updated: 08/07/2026, 20:48:24
# Write your MySQL query statement below
SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;