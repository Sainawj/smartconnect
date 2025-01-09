import os

class Config:
    # Security
    SECRET_KEY = '4c9435a6782ad9a271c6512b7e75c0b9b0d50868838376891a8d72cb877bc3a6'  # Replace this with your actual security key

    # MongoDB Configuration
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/smartconnect')  # Default URI to local MongoDB instance

    # JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'e6983b9f9b33b8f7d88725ac6c849e14389cced6a222a58391a274062593b290')  # Replace with actual JWT secret key for your app
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Access token expiry in seconds (1 hour)

    # Flask-Login Configuration
    LOGIN_MANAGER_LOGIN_VIEW = 'auth.login'  # Default login route for Flask-Login

    # NLP Model Directory (Optional - Adjust path if necessary)
    NLP_MODEL_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/file_nlp')

    # Other Configuration (Adjust as needed)
    APP_NAME = 'SmartConnect Chatbot'
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True

