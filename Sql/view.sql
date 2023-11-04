CREATE OR REPLACE VIEW AllProducts AS
SELECT
    p.name AS product_name,
    p.price AS product_price,
    c.name AS category_name,
    b.name AS brand_name
FROM
    Product p
    JOIN Category c ON p.category_id = c.id
    JOIN Brand b ON p.brand_id = b.id;

CREATE OR REPLACE VIEW AllProductsId AS
SELECT
    p.id AS product_id
FROM
    Product p
;

CREATE OR REPLACE VIEW Last10Products AS
SELECT 
    p.name AS product_name,
    p.price AS product_price,
    c.name AS category_name,
    b.name AS brand_name
FROM Product p
JOIN Category c ON p.category_id = c.id
JOIN Brand b ON p.brand_id = b.id
ORDER BY p.id DESC
LIMIT 10;


CREATE OR REPLACE VIEW GetAllCategories AS
SELECT
    c.name AS category_name
FROM
    Category c;


CREATE OR REPLACE VIEW GetAllBrands AS
SELECT
    b.name AS brand_name
FROM
    Brand b;