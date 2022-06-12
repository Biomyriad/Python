from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.sender = data['sender']
        self.sender_name = data['sender_name']
        self.recipient = data['recipient']
        self.recipient_name = data['recipient_name']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_id(cls, id):
        query = f"""
            select messages.*, users.first_name as recipient_name, sent_by.first_name as sender_name
            from users
            left join messages on messages.recipient = users.id
            left join users as sent_by on messages.sender = sent_by.id
            where messages.id = %(id)s;
        """
        data = { "id": id }
        results = cls.run_query(query, data)

        # try:
        item = cls(results[0])
        # except Exception as e:
        #     return False

        return item

    @classmethod
    def get_messages_by_recipient_id(cls, id):
        query = f"""
            select messages.*, users.first_name as recipient_name, sent_by.first_name as sender_name
            from users
            left join messages on messages.recipient = users.id
            left join users as sent_by on messages.sender = sent_by.id
            where users.id = %(id)s;
        """

        data = {'id': id}
        results = cls.run_query(query, data)
        items = []
        for row in results:
            print(row)
            items.append( cls(row) )
        return items  

    @classmethod
    def save(cls, data ):
        query = f"""
            INSERT INTO messages ( sender, recipient, message, created_at, updated_at) 
            VALUES ( %(sender)s, %(recipient)s, %(message)s, NOW(), NOW() );
        """
        return cls.run_query(query, data)

    @classmethod
    def delete_by_id(cls, id ):
        query = "DELETE FROM messages WHERE id=%(id)s;"
        data = { "id": id }
        return cls.run_query( query, data )  

    @classmethod
    def run_query(cls, query, data=None):
        return connectToMySQL('private_wall').query_db( query, data )