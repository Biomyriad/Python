from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

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
            SELECT *
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
            SELECT *
            FROM users 
            WHERE id=%(id)s;
        """
        data = { "id": id }
        results = cls.run_query(query, data)

        if len(results) > 1:
            item = cls(results[0])
        else:
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
    def update(cls, data ):
        query = f"""
            UPDATE recipes 
            SET posted_by=%(posted_by)s, 
            name=%(name)s , 
            date_made=%(date_made)s , 
            is_under_30min=%(is_under_30min)s , 
            description=%(description)s , 
            instructions=%(instructions)s , 
            updated_at=NOW() 
            WHERE id=%(id)s;
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

        return is_valid
