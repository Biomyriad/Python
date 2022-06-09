from flask import flash
import re
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password_hash = data['password_hash']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = f"""
            SELECT * 
            FROM users;
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
            FROM users 
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
            FROM users 
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
            INSERT INTO users ( first_name, last_name, email, password_hash, created_at, updated_at) 
            VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password_hash)s, NOW(), NOW() );
        """
        return cls.run_query(query, data)

    @classmethod
    def delete_by_id(cls, id ):
        query = "DELETE FROM users WHERE id=%(id)s;"
        data = { "id": id }
        return cls.run_query( query, data )  

    @classmethod
    def run_query(cls, query, data=None):
        return connectToMySQL('login_and_register').query_db( query, data )

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