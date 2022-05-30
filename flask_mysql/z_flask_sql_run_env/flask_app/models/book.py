from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    DB_AND_TABLE =('books', 'books')
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
            INSERT INTO {cls.DB_AND_TABLE[1]} ( title , num_of_pages , created_at , updated_at ) 
            VALUES ( %(title)s , %(num_of_pages)s , NOW() , NOW() );
        """
        return cls.run_query(query, data)

    @classmethod
    def update(cls, data ):
        query = f"""
            UPDATE {cls.DB_AND_TABLE[1]} 
            SET title=%(title)s , title=%(num_of_pages)s , updated_at=NOW() 
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

