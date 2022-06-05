from ast import Try
from flask import flash
import re
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = f"""
            SELECT * 
            FROM emails;
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
            FROM emails 
            WHERE id=%(id)s;
        """
        data = { "id": id }
        results = cls.run_query(query, data)

        try:
            item = cls(results[0])
        except Exception as e:
            return False

        return item

    @classmethod
    def get_by_email(cls, email):
        query = f"""
            SELECT * 
            FROM emails 
            WHERE email=%(email)s;
        """
        data = { "email": email }
        results = cls.run_query(query, data)

        try:
            item = cls(results[0])
        except Exception as e:
            return False

        return item

    @classmethod
    def save(cls, data ):
        query = f"""
            INSERT INTO emails ( email ) 
            VALUES ( %(email)s );
        """
        return cls.run_query(query, data)

    @classmethod
    def delete_by_id(cls, id ):
        query = "DELETE FROM emails WHERE id=%(id)s;"
        data = { "id": id }
        return cls.run_query( query, data )  

    @classmethod
    def run_query(cls, query, data=None):
        return connectToMySQL('email_validation').query_db( query, data )

    @staticmethod
    def validate(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if not Email.get_by_email(data['email']) == False:
            flash('Email has already been submitted!')
            is_valid = False

        if is_valid:
            flash(f'The email address you entered ({data["email"]}) is a VALID email address! Thank you!')
        return is_valid