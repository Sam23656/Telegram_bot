INSERT INTO Client(chat_id, is_admin, name, surname, phone, email, address)
VALUES
(143956182, true, 'John', 'Doe', '+123456789', 'wZ7pI@example.com', '123 Main St');

INSERT INTO Category(name)
VALUES
('Electronics'),
('Clothing');

INSERT INTO Product(name, description, category_id, price)
VALUES
('iPhone 15', 'The latest iPhone', 1, 999.99),
('T-Shirt', 'A comfortable shirt', 2, 19.99);

