INSERT INTO Client(chat_id, is_admin, name, surname, phone, email, address)
VALUES
(143956182, true, 'John', 'Doe', '+123456789', 'wZ7pI@example.com', '123 Main St');

INSERT INTO Category(name)
VALUES
('Electronics'),
('Clothing');

INSERT INTO Product(id ,name, description, category_id, price)
VALUES
(gen_random_uuid(),'iPhone 15', 'The latest iPhone', 1, 999.99),
(gen_random_uuid(),'T-Shirt', 'A comfortable shirt', 2, 19.99),
(gen_random_uuid(),'Jeans', 'A pair of jeans', 2, 29.99),
(gen_random_uuid(),'Socks', 'A pair of socks', 2, 9.99),
(gen_random_uuid(),'Shoes', 'A pair of shoes', 2, 49.99);

