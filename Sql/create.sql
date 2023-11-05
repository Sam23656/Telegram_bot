CREATE DATABASE Product_Shop;
\c product_shop;

CREATE TABLE Client(
    id SERIAL PRIMARY KEY,
    chat_id INT UNIQUE,
    is_admin BOOLEAN,
    name VARCHAR(255),
    surname VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE Category(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Brand(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Product(
    id UUID DEFAULT gen_random_uuid() NOT NULL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    category_id INT REFERENCES Category(id),
    brand_id INT REFERENCES Brand(id),
    price DECIMAL(10, 2)
);

CREATE TABLE Orders(
    id SERIAL PRIMARY KEY,
    client_id INT REFERENCES Client(id),
    order_date DATE
);

CREATE TABLE Order_Product(
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES Orders(id),
    product_id UUID REFERENCES Product(id),
    quantity INT
);

CREATE TABLE Cart(
    id SERIAL PRIMARY KEY,
    client_id INT REFERENCES Client(id)
);

CREATE TABLE Cart_Product(
    id SERIAL PRIMARY KEY,
    cart_id INT REFERENCES Cart(id),
    product_id UUID REFERENCES Product(id),
    quantity INT
);


CREATE INDEX idx_client_chat_id ON Client (chat_id);
CREATE INDEX idx_category_name ON Category (name);
CREATE INDEX idx_product_name ON Product (name);
CREATE INDEX idx_product_category_id ON Product (category_id);
CREATE INDEX idx_orders_client_id ON Orders (client_id);
CREATE INDEX idx_order_product_order_id ON Order_Product (order_id);
CREATE INDEX idx_order_product_product_id ON Order_Product (product_id);
CREATE INDEX idx_cart_client_id ON Cart (client_id);
CREATE INDEX idx_cart_product_id ON Cart_Product (cart_id);
CREATE INDEX idx_cart_product_product_id ON Cart_Product (product_id);

