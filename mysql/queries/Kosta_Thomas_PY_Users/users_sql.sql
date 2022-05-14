-- Create 3 new users
INSERT INTO users (users.first_name, last_name, email) values('John', 'Smith', 'john.s@sql.com');
INSERT INTO users (first_name, last_name, email) values('Jane', 'Doe', 'jane.d@sql.com');
INSERT INTO users (first_name, last_name, email) values('Peter', 'Parker', 'peter.p@sql.com');

-- Retrieve all the users
SELECT * FROM users;

-- Retrieve the first user using their email address
SELECT * FROM users WHERE email = 'john.s@sql.com';

-- Retrieve the last user using their id
SELECT * FROM users WHERE id = LAST_INSERT_ID();

-- Change the user with id=3 so their last name is Pancakes
UPDATE users SET last_name = 'Pancakes' WHERE id = 3;

-- Delete the user with id=2 from the database
DELETE FROM users WHERE id = 2;

-- Get all the users, sorted by their first name
SELECT * FROM users ORDER BY first_name;

-- Get all the users, sorted by their first name in descending order
SELECT * FROM users ORDER BY first_name DESC;

