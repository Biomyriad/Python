from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.posted_by_id = data['posted_by']
        self.name = data['name']
        self.date_made = data['date_made']
        self.is_under_30min = data['is_under_30min']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = f"""
            SELECT *
            FROM recipes;
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
            FROM recipes 
            WHERE id=%(id)s;
        """
        data = { "id": id }
        results = cls.run_query(query, data)

        if len(results) > 0:
            item = cls(results[0])
        else:
            return False

        return item

    @classmethod
    def save(cls, data ):
        query = f"""
            INSERT INTO recipes ( posted_by, name, date_made, is_under_30min, description, instructions, created_at, updated_at) 
            VALUES ( %(posted_by)s, %(name)s, %(date_made)s, %(is_under_30min)s, %(description)s, %(instructions)s, NOW(), NOW() );
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
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        data = { "id": id }
        return cls.run_query( query, data )  

    @classmethod
    def run_query(cls, query, data=None):
        return connectToMySQL('recipes').query_db( query, data )

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3 or data['name'] == "":
            flash({"label": "name", "message": "Name must be greater than 3 letters."},"recipe")
            is_valid = False

        if data['date_made'] == "":
            flash({"label": "date_made", "message": "Must enter a date."},"recipe")
            is_valid = False

        if len(data['description']) < 3 or data['description'] == "":
            flash({"label": "description", "message": "Description must be greater than 3 letters."},"recipe")
            is_valid = False

        if len(data['instructions']) < 3 or data['instructions'] == "":
            flash({"label": "instructions", "message": "Instructions must be greater than 3 letters."},"recipe")
            is_valid = False                                 

        return is_valid
