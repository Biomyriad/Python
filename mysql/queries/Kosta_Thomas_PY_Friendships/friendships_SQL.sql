-- Create 6 new users
INSERT INTO users (first_name, last_name) VALUES('Amy', 'Giver'),('Eli', 'Byers'),('Marky', 'Mark'),('Big', 'Bird'),('Kermit', 'The Frog'),('Oscar', 'The Grouch');

-- Have user 1 be friends with user 2, 4 and 6
INSERT INTO friendships (user_id, friend_id) VALUES(1, 2),(1, 4),(1, 6);

-- Have user 2 be friends with user 1, 3 and 5
INSERT INTO friendships (user_id, friend_id) VALUES(2, 1),(2, 3),(2, 5);

-- Have user 3 be friends with user 2 and 5
INSERT INTO friendships (user_id, friend_id) VALUES(3, 2),(3, 5);

-- Have user 4 be friends with user 3
INSERT INTO friendships (user_id, friend_id) VALUES(4, 3);

-- Have user 5 be friends with user 1 and 6
INSERT INTO friendships (user_id, friend_id) VALUES(5, 1),(5, 6);

-- Have user 6 be friends with user 2 and 3
INSERT INTO friendships (user_id, friend_id) VALUES(6, 2),(6, 3);

-- Display the relationships create as shown in the above image
SELECT users1.first_name, users1.last_name, users2.first_name, users2.last_name FROM users AS users1
JOIN friendships ON users1.id = friendships.user_id
LEFT JOIN users AS users2 ON friendships.friend_id = users2.id;

-- Return all users who are friends with the first user, make sure their names are displayed in results.
SELECT users1.first_name, users1.last_name, CONCAT('Are friends with ', users2.first_name, ' ', users2.last_name) AS friend FROM users AS users1
JOIN friendships ON users1.id = friendships.user_id
LEFT JOIN users AS users2 ON friendships.friend_id = users2.id
WHERE friendships.friend_id = 1;

-- Return the count of all friendships
SELECT COUNT(*) FROM friendships;

-- Find out who has the most friends and return the count of their friends.
--  # DOES NOT ACCOUNT FOR USERS WHO ARE TIED FOR MOST FRIENDS.
SELECT users.first_name, COUNT(*) AS most_friends
FROM friendships
JOIN users ON friendships.user_id = users.id
GROUP BY user_id
ORDER BY most_friends DESC
LIMIT 1;

-- Return the friends of the third user in alphabetical order
SELECT users1.first_name, users1.last_name AS friend FROM users AS users1
JOIN friendships ON users1.id = friendships.user_id
LEFT JOIN users AS users2 ON friendships.friend_id = users2.id
WHERE friendships.friend_id = 3
ORDER BY users1.first_name;