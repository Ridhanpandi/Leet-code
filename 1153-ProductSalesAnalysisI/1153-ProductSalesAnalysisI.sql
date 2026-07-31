-- Last updated: 31/07/2026, 08:53:36
SELECT
    product_name,
    year,
    price
FROM Sales
LEFT JOIN Product
ON Sales.product_id = Product.product_id;