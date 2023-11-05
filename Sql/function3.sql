CREATE OR REPLACE FUNCTION get_user_is_admin(user_id INT)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN (SELECT is_admin FROM Client WHERE id = user_id);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_all_products_for_xlsx()
RETURNS TABLE (
    product_name VARCHAR(255),
    product_description VARCHAR(255),
    product_price DECIMAL(10, 2),
    category_id INT,
    category_name VARCHAR(255),
    brand_id INT,
    brand_name VARCHAR(255)
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.name AS product_name,
        p.description AS product_description,
        p.price AS product_price,
        p.category_id AS category_id,
        c.name AS category_name,
        p.brand_id AS brand_id,
        b.name AS brand_name
    FROM
        Product p
        JOIN Category c ON p.category_id = c.id
        JOIN Brand b ON p.brand_id = b.id;
END;
$$ LANGUAGE plpgsql;
