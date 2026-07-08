-- Last updated: 08/07/2026, 20:49:48
# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT DISTINCT customerId 
    FROM Orders
);