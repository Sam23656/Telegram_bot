CREATE OR REPLACE VIEW ProductsWithCategories AS
SELECT
    p.name AS product_name,
    p.description AS product_description,
    p.price AS product_price,
    c.name AS category_name
FROM
    Product p
    JOIN Category c ON p.category_id = c.id;


CREATE OR REPLACE VIEW Last5Products AS
SELECT 
    p.name AS product_name,
    p.description AS product_description,
    p.price AS product_price,
    c.name AS category_name
FROM Product p
JOIN Category c ON p.category_id = c.id
ORDER BY p.id DESC
LIMIT 5;
