from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fav_by_author = []

    @classmethod
    def get_all(cls):
        query = f"""
            SELECT * 
            FROM books;
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
            FROM books 
            WHERE id=%(id)s;
        """
        data = { "id": id }
        results = cls.run_query(query, data)
        item = cls(results[0])
        return item

    @classmethod
    def get_books_fav_by_author(cls, id):
        query = f"""
            SELECT books.*, author_results.*
            FROM  ( SELECT favorites.*, authors.*
                    FROM authors
                    LEFT JOIN favorites on authors.id = favorites.author_id
                    WHERE book_id = %(id)s

                    UNION

                    SELECT null as "author_id", null as "book_id", authors.*
                    FROM authors
                    WHERE authors.id not in ( SELECT author_id
                                            FROM favorites
                                            WHERE book_id = %(id)s)
                    ) as author_results
            LEFT JOIN books on books.id = author_results.book_id
            union
            select books.*, null as "author_id", null as "book_id", null as "author_results.id", null as "name", null as "author_results.created_at", null as "author_results.updated_at"
            from books
            where books.id = %(id)s and books.id not in (select book_id from favorites);
        """

        data = { "id": id }
        results = cls.run_query(query, data)

        authors_not_favorite_books = []
        
        if not results[0]["id"] == None:
            book = cls(results[0])
        else:
            for row_id in range(0, len(results)):
                if not results[row_id]["id"] == None:
                    book = cls(results[row_id])
                    break

        for row in results:
            if row['.id'] is None:
                continue
            author_data = {
                'id': row['.id'],
                'name': row['name'],
                'created_at': row['.created_at'],
                'updated_at': row['.updated_at']
            }
            
            if row['id'] == data['id']:
                book.fav_by_author.append( author.Author(author_data) )
            else:
                authors_not_favorite_books.append( author.Author(author_data) )

        return (book, authors_not_favorite_books)        

    @classmethod
    def save(cls, data ):
        query = f"""
            INSERT INTO books ( title , num_of_pages , created_at , updated_at ) 
            VALUES ( %(title)s , %(num_of_pages)s , NOW() , NOW() );
        """
        return cls.run_query(query, data)
        
    @classmethod
    def run_query(cls, query, data=None):
        return connectToMySQL('books').query_db( query, data )

