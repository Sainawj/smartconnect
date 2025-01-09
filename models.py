from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

mongo = PyMongo()

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = datetime.utcnow()
        self.last_login = None

    def save(self):
        hashed_password = generate_password_hash(self.password)
        user_data = {
            'username': self.username,
            'email': self.email,
            'password': hashed_password,
            'created_at': self.created_at,
            'last_login': self.last_login
        }
        mongo.db.users.insert_one(user_data)

    @classmethod
    def get_by_username(cls, username):
        return mongo.db.users.find_one({'username': username})

    @classmethod
    def get_by_email(cls, email):
        return mongo.db.users.find_one({'email': email})

    @classmethod
    def get_by_id(cls, user_id):
        return mongo.db.users.find_one({'_id': user_id})
