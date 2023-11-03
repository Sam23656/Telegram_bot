CREATE DATABASE Product_Shop;
\c product_shop;

CREATE TABLE Client(
    id SERIAL PRIMARY KEY,
    chat_id INT,
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

CREATE TABLE Product(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    category_id INT REFERENCES Category(id),
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
    product_id INT REFERENCES Product(id),
    quantity INT
);


