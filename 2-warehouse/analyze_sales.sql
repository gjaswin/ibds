-- Total sales by product category
SELECT
    p.category,
    SUM(s.total_amount) AS total_sales
FROM
    Sales s
JOIN
    Product p ON s.product_id = p.product_id
GROUP BY
    p.category;

-- Total sales by customer region --
SELECT
    c.region,
    SUM(s.total_amount) AS total_sales
FROM
    Sales s
JOIN
    Customer c ON s.customer_id = c.customer_id
GROUP BY
    c.region;