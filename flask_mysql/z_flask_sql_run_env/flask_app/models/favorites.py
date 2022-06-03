from flask_app.config.mysqlconnection import connectToMySQL

class Favorites:
    def __init__(self, data):
        self.author_id = data["author_id"]
        self.book_id = data["book_id"]

    @classmethod
    def save(cls, data ):
        query = f"""
            INSERT INTO favorites ( author_id , book_id ) 
            VALUES ( %(author_id)s , %(book_id)s );
        """
        return cls.run_query(query, data)

    @classmethod
    def run_query(cls, query, data=None):
        return connectToMySQL('books').query_db( query, data )