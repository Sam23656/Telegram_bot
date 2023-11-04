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


CREATE OR REPLACE FUNCTION get_product_by_id(product_id UUID)
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


CREATE OR REPLACE FUNCTION delete_product_by_id(product_id UUID)
RETURNS VOID AS $$
BEGIN
    DELETE FROM Product WHERE id = product_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_category_id_by_name(category_name VARCHAR(255))
RETURNS INT AS $$
BEGIN
    RETURN (SELECT id FROM Category WHERE name = category_name);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_brand_id_by_name(brand_name VARCHAR(255))
RETURNS INT AS $$
BEGIN
    RETURN (SELECT id FROM Brand WHERE name = brand_name);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION add_product(
    name VARCHAR(255),
    description VARCHAR(255),
    category_id INT,
    brand_id INT,
    price DECIMAL(10, 2)
) RETURNS VOID AS $$
BEGIN
    INSERT INTO Product(id, name, description, category_id, brand_id, price)
    VALUES (gen_random_uuid(),name, description, category_id, brand_id, price);
END;
$$ LANGUAGE plpgsql