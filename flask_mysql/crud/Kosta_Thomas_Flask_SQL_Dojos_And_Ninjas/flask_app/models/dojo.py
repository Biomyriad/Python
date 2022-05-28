from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = cls.run_query(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        data = { "id": id }
        results = cls.run_query(query, data)
        ninja = cls(results[0])
        return ninja

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return cls.run_query(query, data)

    @classmethod
    def update(cls, data ):
        query = "UPDATE dojos SET first_name=%(name)s , updated_at=NOW() WHERE id=%(id)s;"
        return cls.run_query(query, data)

    @classmethod
    def delete_by_id(cls, id ):
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        data = { "id": id }
        return cls.run_query(query, data)
    @classmethod
    def run_query(cls, query, data=None):
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )

