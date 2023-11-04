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
