SELECT * FROM USERS;
INSERT INTO users (first_name, last_name) values('John', 'Smith');
UPDATE users SET first_name = 'jane', last_name = 'Doe' WHERE id = 6;
DELETE FROM users WHERE id = 6;