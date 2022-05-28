from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = cls.run_query(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        data = { "id": id }
        results = cls.run_query(query, data)
        ninja = cls(results[0])
        return ninja

    @classmethod
    def get_all_by_dojo_id(cls, id):
        query = "SELECT * FROM ninjas WHERE dojo_id=%(id)s;"
        data = { "id": id }
        results = cls.run_query(query, data)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id , created_at , updated_at ) VALUES ( %(fname)s , %(lname)s , %(age)s , %(dojo_id)s , NOW() , NOW() );"
        return cls.run_query(query, data)

    @classmethod
    def update(cls, data ):
        query = "UPDATE ninjas SET first_name=%(fname)s , last_name=%(lname)s , email=%(email)s , age=%(age)s , dojo_id=%(dojo_id)s , updated_at=NOW() WHERE id=%(id)s;"
        return cls.run_query(query, data)

    @classmethod
    def delete_by_id(cls, id ):
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        data = { "id": id }
        return cls.run_query(query, data)

    @classmethod
    def run_query(cls, query, data=None):
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )