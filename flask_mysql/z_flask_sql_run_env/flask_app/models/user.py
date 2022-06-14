from flask import flash
import re
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
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
            SELECT id, first_name, last_name, email, created_at, updated_at
            FROM users;
        """
        results = cls.run_query(query)
        items = []
        for row in results:
            row["password_hash"] = ''
            items.append( cls(row) )
        return items    

    @classmethod
    def get_by_id(cls, id):
        query = f"""
            SELECT id, first_name, last_name, email, created_at, updated_at 
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
            SELECT id, first_name, last_name, email, created_at, updated_at 
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
    def get_by_email_with_hash(cls, email):
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
        return connectToMySQL('private_wall').query_db( query, data )

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data['first_name']) < 2 or data['first_name'] == "":
            flash({"label": "first_name", "message": "First name must be greater than 2 letters."},"register")
            is_valid = False
        if len(data['last_name']) < 2 or data['last_name'] == "":
            flash({"label": "last_name", "message": "First name bust be greater than 2 letters."},"register")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash({"label": "email", "message": "Invalid email address."},"register")
            is_valid = False
        elif not User.get_by_email(data['email']) == False:
            flash({"label": "email", "message": "Email address has already been registered."},"register")
            is_valid = False
        return is_valid