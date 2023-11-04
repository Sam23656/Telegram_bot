CREATE OR REPLACE FUNCTION get_products_by_category(category_name VARCHAR(255))
RETURNS TABLE (
    product_name VARCHAR(255),
    product_description VARCHAR(255),
    product_price DECIMAL(10, 2)
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.name AS product_name,
        p.description AS product_description,
        p.price AS product_price
    FROM
        Product p
        JOIN Category c ON p.category_id = c.id
    WHERE
        c.name = category_name;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_products_by_brand(brand_name VARCHAR(255))
RETURNS TABLE (
    product_name VARCHAR(255),
    product_description VARCHAR(255),
    product_price DECIMAL(10, 2)
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.name AS product_name,
        p.description AS product_description,
        p.price AS product_price
    FROM
        Product p
        JOIN Brand b ON p.brand_id = b.id
    WHERE
        b.name = brand_name;
END;
$$ LANGUAGE plpgsql;


CREATE FUNCTION get_product_by_id(product_id UUID)
RETURNS TABLE (
    product_name VARCHAR(255),
    product_description VARCHAR(255),
    product_price DECIMAL(10, 2),
    category_name VARCHAR(255),
    brand_name VARCHAR(255)
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.name AS product_name,
        p.description AS product_description,
        p.price AS product_price,
        c.name AS category_name,
        b.name AS brand_name
    FROM
        Product p
        JOIN Category c ON p.category_id = c.id
        JOIN Brand b ON p.brand_id = b.id
    WHERE
        p.id = product_id;
END;
$$ LANGUAGE plpgsql;