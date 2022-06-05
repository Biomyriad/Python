from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_id(cls, id):
        query = f"""
            SELECT * 
            FROM dojos 
            WHERE id=%(id)s;
        """
        data = { "id": id }
        results = cls.run_query(query, data)
        item = cls(results[0])
        return item

    @classmethod
    def save(cls, data ):
        query = f"""
            INSERT INTO dojos ( name , location , language , comment , created_at , updated_at ) 
            VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s , NOW() , NOW());
        """
        row_id = cls.run_query(query, data)
        return row_id

    @classmethod
    def run_query(cls, query, data=None):
        return connectToMySQL('dojo_survey').query_db( query, data )

    @staticmethod
    def validate(data):
        is_valid = True # we assume this is true
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if 'location' not in data:
            flash("Must pick a location.")
            is_valid = False
        if 'language' not in data:
            flash("Must pick a language.")
            is_valid = False
        return is_valid