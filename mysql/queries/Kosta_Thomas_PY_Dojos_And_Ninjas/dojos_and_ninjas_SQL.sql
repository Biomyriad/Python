-- Create 3 new dojos
INSERT INTO dojos (name) VALUES('Bellevue');
INSERT INTO dojos (name) VALUES('New York');
INSERT INTO dojos (name) VALUES('Dallas');

-- Delete the 3 dojos you just created
DELETE FROM dojos WHERE id < 4;

-- Create 3 more dojos
INSERT INTO dojos (name) VALUES('Seattle');
INSERT INTO dojos (name) VALUES('DC');
INSERT INTO dojos (name) VALUES('Wichita');

-- Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Jane', 'Doe', '18', 1);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('John', 'Doe', '20', 1);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('James', 'Smith', '34', 1);

-- Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Jan', 'Post', '28', 2);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Steve', 'Post', '31', 2);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Tim', 'Bert', '19', 2);

-- Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Ben', 'Lock', '17', 3);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Jim', 'Car', '44', 3);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Rob', 'Hollow', '41', 3);

-- Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas WHERE dojo_id = 1;

-- Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas WHERE dojo_id = 3;

-- Retrieve the last ninja's dojo
SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id ORDER BY ninjas.id DESC LIMIT 1;