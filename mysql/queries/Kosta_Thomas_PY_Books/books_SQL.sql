-- Create 5 different authors: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu
INSERT INTO authors (name) VALUES('Jane Austen');
INSERT INTO authors (name) VALUES('Emily Dickinson');
INSERT INTO authors (name) VALUES('Fyodor Dostoevsky');
INSERT INTO authors (name) VALUES('William Shakespeare');
INSERT INTO authors (name) VALUES('Lau Tzu');

-- Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
INSERT INTO books (title, num_of_pages) VALUES('C Sharp', '142');
INSERT INTO books (title, num_of_pages) VALUES('Java', '298');
INSERT INTO books (title, num_of_pages) VALUES('Python', '120');
INSERT INTO books (title, num_of_pages) VALUES('PHP', '98');
INSERT INTO books (title, num_of_pages) VALUES('Ruby', '100');

-- Change the name of the C Sharp book to C#
-- IN SUBQUERY, MUST CREATE TEMP COPY OF TABLE (select * from books) AND IT MUST HAVE AN ALIAS *IE tmp_books
UPDATE books SET title = 'C#' WHERE books.id = (SELECT tmp_books.id FROM (SELECT * FROM books) tmp_books WHERE tmp_books.title = 'C Sharp');

-- Change the first name of the 4th author to Bill
UPDATE authors SET name = 'Bill Shakespeare' WHERE id = 4;

-- Have the first author favorite the first 2 books
INSERT INTO favorites (author_id, book_id) VALUES(1, 2);

-- Have the second author favorite the first 3 books
INSERT INTO favorites (author_id, book_id) VALUES(2, 3);

-- Have the third author favorite the first 4 books
INSERT INTO favorites (author_id, book_id) VALUES(3, 4);

-- Have the fourth author favorite all the books
INSERT INTO favorites (author_id, book_id) VALUES(4, 1),(4, 2),(4, 3),(4, 4),(4, 5);

-- Retrieve all the authors who favorited the 3rd book
SELECT name FROM authors JOIN favorites ON authors.id = favorites.author_id WHERE favorites.book_id = 3;

-- Remove the first author of the 3rd book's favorites
DELETE FROM favorites 
WHERE favorites.author_id = 
    (SELECT id FROM authors 
     JOIN 
        (SELECT * FROM favorites) 
        favs ON authors.id = favs.author_id
         WHERE favs.book_id = 3 LIMIT 1);

-- Add the 5th author as an other who favorited the 2nd book
INSERT INTO favorites (author_id, book_id) VALUES(5, 2);

-- Find all the books that the 3rd author favorited
SELECT title FROM books
JOIN favorites ON books.id = favorites.book_id
JOIN authors ON favorites.author_id = authors.id
WHERE author_id = 3;

-- Find all the authors that favorited to the 5th book
SELECT name FROM authors
JOIN favorites ON authors.id = favorites.author_id
JOIN books ON favorites.book_id = books.id
WHERE book_id = 5;