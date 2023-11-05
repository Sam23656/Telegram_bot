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
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION update_product(
    product_id UUID,
    product_name VARCHAR(255),
    product_description VARCHAR(255),
    product_category_id INT,
    product_brand_id INT,
    product_price DECIMAL(10, 2)
) RETURNS VOID AS $$
BEGIN
    UPDATE Product
    SET
        name = product_name,
        description = product_description,
        category_id = product_category_id,
        brand_id = product_brand_id,
        price = product_price
    WHERE
        id = product_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION add_or_update_client(
    client_chat_id INT,
    is_admin BOOLEAN,
    name VARCHAR(255),
    surname VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255)
) RETURNS VOID AS $$
BEGIN
    INSERT INTO Client (chat_id, is_admin, name, surname, phone, email, address)
    VALUES (client_chat_id, is_admin, name, surname, phone, email, address)
    ON CONFLICT (chat_id)
    DO UPDATE
    SET
        is_admin = EXCLUDED.is_admin,
        name = EXCLUDED.name,
        surname = EXCLUDED.surname,
        phone = EXCLUDED.phone,
        email = EXCLUDED.email,
        address = EXCLUDED.address;

    INSERT INTO Cart (client_id)
    SELECT id
    FROM Client
    WHERE chat_id = client_chat_id
    ON CONFLICT DO NOTHING;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_client_info_by_chat_id(client_chat_id INT)
RETURNS TABLE (
    client_is_admin BOOLEAN,
    name VARCHAR(255),
    surname VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255)
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.is_admin AS client_is_admin,
        c.name,
        c.surname,
        c.phone,
        c.email,
        c.address
    FROM
        Client c
    WHERE
        c.chat_id = client_chat_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_client_cart_id(client_chat_id INT)
RETURNS INT AS $$
DECLARE
    cart_id INT;
BEGIN
    SELECT id INTO cart_id
    FROM Cart
    WHERE client_id = (SELECT id FROM Client WHERE chat_id = client_chat_id);
    
    RETURN cart_id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION add_product_to_cart(
    cart_id INT,
    product_id UUID,
    quantity INT
) RETURNS VOID AS $$
BEGIN
    INSERT INTO Cart_Product (cart_id, product_id, quantity)
    VALUES (cart_id, product_id, quantity);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_product_id_by_name(product_name VARCHAR(255))
RETURNS UUID AS $$
BEGIN
    RETURN (SELECT id FROM Product WHERE name = product_name);
END;
$$ LANGUAGE plpgsql;