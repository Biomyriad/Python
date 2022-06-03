from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    @classmethod
    def get_all(cls):
        query = f"""
            SELECT * 
            FROM authors;
        """
        results = cls.run_query(query)
        items = []
        for row in results:
            items.append( cls(row) )
        return items

    @classmethod
    def get_by_id(cls, id):
        query = f"""
            SELECT * 
            FROM authors 
            WHERE id=%(id)s;
        """
        data = { "id": id }
        results = cls.run_query(query, data)
        item = cls(results[0])
        return item

    @classmethod
    def get_authors_fav_books(cls, id):
        query = f"""
            SELECT authors.*, book_results.*
            FROM  ( SELECT favorites.*, books.*
                    FROM books
                    LEFT JOIN favorites on books.id = favorites.book_id
                    WHERE author_id = %(id)s

                    UNION

                    SELECT null as "author_id", null as "book_id", books.*
                    FROM books
                    WHERE books.id not in ( SELECT book_id
                                            FROM favorites
                                            WHERE author_id = %(id)s)
                    ) as book_results
            LEFT JOIN authors on authors.id = book_results.author_id
            union
            select authors.*, null as "author_id", null as "book_id", null as "book_results.id", null as "title", null as "num_of_pages", null as "book_results.created_at", null as "book_results.updated_at"
            from authors
            where authors.id = %(id)s and authors.id not in (select author_id from favorites);
        """

        data = { "id": id }
        results = cls.run_query(query, data)

        not_favorited_books = []

        if not results[0]["id"] == None:
            author = cls(results[0])
        else:
            for row_id in range(0, len(results)):
                if not results[row_id]["id"] == None:
                    author = cls(results[row_id])
                    break

        for row in results:
            if row['.id'] is None:
                continue
            book_data = {
                'id': row['.id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages'],
                'created_at': row['.created_at'],
                'updated_at': row['.updated_at']
            }

            if row['id'] == data['id']:
                author.favorite_books.append( book.Book(book_data) )
            else:
                not_favorited_books.append( book.Book(book_data) )

        return (author, not_favorited_books)

    @classmethod
    def save(cls, data ):
        query = f"""
            INSERT INTO authors ( name, created_at , updated_at ) 
            VALUES ( %(name)s , NOW() , NOW() );
        """
        return cls.run_query(query, data)

    @classmethod
    def run_query(cls, query, data=None):
        return connectToMySQL('books').query_db( query, data )
