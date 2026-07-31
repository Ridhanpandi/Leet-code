-- Last updated: 31/07/2026, 08:53:40
# Write your MySQL query statement below

SELECT  customer_id FROM Customer GROUP BY customer_id
HAVING COUNT(distinct product_key) = (SELECT COUNT(product_key) FROM Product)