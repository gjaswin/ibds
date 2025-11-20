INSERT INTO Customer (customer_id, customer_name, region) VALUES
(1, 'Alice Smith', 'East'),
(2, 'Bob Johnson', 'West'),
(3, 'Charlie Brown', 'North'),
(4, 'Diana Prince', 'South'),
(5, 'Eve Adams', 'East');

INSERT INTO Product (product_id, product_name, category, price) VALUES
(101, 'Laptop', 'Electronics', 1200.00),
(102, 'Mouse', 'Electronics', 25.00),
(103, 'Desk Chair', 'Furniture', 150.00),
(104, 'Keyboard', 'Electronics', 75.00),
(105, 'Monitor', 'Electronics', 300.00),
(106, 'Table', 'Furniture', 200.00);

INSERT INTO Sales (customer_id, product_id, sale_date, quantity, total_amount) VALUES
(1, 101, '2025-01-10', 1, 1200.00),
(1, 102, '2025-01-10', 2, 50.00),
(2, 103, '2025-01-15', 1, 150.00),
(3, 101, '2025-01-20', 1, 1200.00),
(4, 104, '2025-01-22', 1, 75.00),
(5, 105, '2025-01-25', 1, 300.00),
(1, 103, '2025-01-28', 1, 150.00),
(2, 101, '2025-02-01', 1, 1200.00),
(3, 106, '2025-02-05', 1, 200.00),
(4, 102, '2025-02-08', 3, 75.00);