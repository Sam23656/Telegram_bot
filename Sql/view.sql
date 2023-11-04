CREATE OR REPLACE VIEW ProductsWithCategories AS
SELECT
    p.name AS product_name,
    p.description AS product_description,
    p.price AS product_price,
    c.name AS category_name,
    b.name AS brend_name
FROM
    Product p
    JOIN Category c ON p.category_id = c.id
    JOIN Brend b ON p.brend_id = b.id;


CREATE OR REPLACE VIEW Last10Products AS
SELECT 
    p.name AS product_name,
    p.description AS product_description,
    p.price AS product_price,
    c.name AS category_name,
    b.name AS brend_name
FROM Product p
JOIN Category c ON p.category_id = c.id
JOIN Brend b ON p.brend_id = b.id
ORDER BY p.id DESC
LIMIT 10;


CREATE OR REPLACE VIEW GetAllCategories AS
SELECT
    c.name AS category_name
FROM
    Category c;