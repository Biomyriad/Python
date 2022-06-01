from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    DB_AND_TABLE =('books', 'authors')
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
            FROM {cls.DB_AND_TABLE[1]};
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
            FROM {cls.DB_AND_TABLE[1]} 
            WHERE id=%(id)s;
        """
        data = { "id": id }
        results = cls.run_query(query, data)
        item = cls(results[0])
        return item

    @classmethod
    def save(cls, data ):
        query = f"""
            INSERT INTO {cls.DB_AND_TABLE[1]} ( name, created_at , updated_at ) 
            VALUES ( %(name)s , NOW() , NOW() );
        """
        return cls.run_query(query, data)

    @classmethod
    def update(cls, data ):
        query = f"""
            UPDATE {cls.DB_AND_TABLE[1]} 
            SET name=%(name)s , updated_at=NOW() 
            WHERE id=%(id)s;
        """
        return cls.run_query(query, data)

    @classmethod
    def delete_by_id(cls, id ):
        query = f"""
            DELETE FROM {cls.DB_AND_TABLE[1]} 
            WHERE id=%(id)s;
        """
        data = { "id": id }
        return cls.run_query(query, data)

    @classmethod
    def run_query(cls, query, data=None):
        return connectToMySQL(cls.DB_AND_TABLE[0]).query_db( query, data )

    @classmethod
    def test(cls, author_id):
        query = f"""
            SELECT * 
            FROM {cls.DB_AND_TABLE[1]}
            left join favorites on authors.id = favorites.author_id
            left join books on favorites.book_id = books.id
            where authors.id = %(id)s;
        """
        data = { "id": author_id }
        results = cls.run_query(query, data)

        author = cls(results[0])
        unfavorited_books = []

        for row in results:
            book_data = {
                'id': row['books.id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }

            if row['id'] == author_id:
                author.favorite_books.append( book.Book(book_data) )
            else:
                

            

        return author