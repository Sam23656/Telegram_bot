INSERT INTO Category(name)
VALUES
('Electronics'),
('Clothing');

INSERT INTO Brand(name)
VALUES
('Apple'),
('Samsung'),
('Adidas'),
('Puma');

INSERT INTO Product(id ,name, description, category_id, brand_id, price)
VALUES
(gen_random_uuid(),'iPhone 14', 'Apple iPhone 14', 1, 1, 1000.00),
(gen_random_uuid(),'Samsung Galaxy S21', 'Samsung Galaxy S21', 1, 2, 800.00),
(gen_random_uuid(),'T-Shirt', 'Cotton T-Shirt', 2, 3, 50.00),
(gen_random_uuid(),'Jeans', 'Cotton Jeans', 2, 4, 80.00);
