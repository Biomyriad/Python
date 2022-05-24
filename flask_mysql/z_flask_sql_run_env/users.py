from mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_byid(cls, id):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        data = { "id": id }
        results = connectToMySQL('users').query_db(query,data)
        user = cls(results[0])
        return user

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('users').query_db( query, data )    

    # @classmethod
    # def update(cls, data ):
    #     query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
    #     return connectToMySQL('users').query_db( query, data )  

    @classmethod
    def delete_byid(cls, id ):
        query = "DELETE FROM users WHERE id=%(id)s;"
        data = { "id": id }
        return connectToMySQL('users').query_db( query, data )  