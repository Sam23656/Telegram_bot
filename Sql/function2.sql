
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
    AND NOT EXISTS (SELECT 1 FROM Cart WHERE client_id = id);
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


CREATE OR REPLACE FUNCTION get_cart_products(client_cart_id INT)
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
        p.id IN (SELECT product_id FROM Cart_Product WHERE cart_id = client_cart_id);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_client_id_by_chat_id(client_chat_id INT)
RETURNS INT AS $$
BEGIN
    RETURN (SELECT id FROM Client WHERE chat_id = client_chat_id);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION create_order(
    client_id INT
) RETURNS INT AS $$
DECLARE
    new_order_id INT;
BEGIN
    INSERT INTO Orders (client_id, order_date)
    VALUES (client_id, NOW())
    RETURNING id INTO new_order_id; 

    RETURN new_order_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION add_product_to_order(
    order_id INT,
    product_id UUID,
    quantity INT
) RETURNS VOID AS $$
BEGIN
    INSERT INTO Order_Product (order_id, product_id, quantity)
    VALUES (order_id, product_id, quantity);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION remove_product_from_cart(
    client_cart_id INT,
    client_product_id UUID
) RETURNS VOID AS $$
BEGIN
    DELETE FROM Cart_Product
    WHERE cart_id = client_cart_id
    AND product_id = client_product_id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION check_client_contact_info(client_id INT)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN (SELECT address IS NOT NULL AND phone IS NOT NULL AND email IS NOT NULL FROM Client WHERE id = client_id);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_product_ids_in_cart(client_cart_id INT)
RETURNS TABLE (product_id UUID) AS $$
BEGIN
    RETURN QUERY
    SELECT cp.product_id
    FROM Cart_Product cp
    JOIN Cart c ON c.id = cp.cart_id
    WHERE c.client_id = client_cart_id;
END;
$$ LANGUAGE plpgsql;

