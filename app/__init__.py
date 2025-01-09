# smartconnect/app/__init__.py

from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_login import LoginManager

# Initialize Flask extensions
mongo = PyMongo()
jwt = JWTManager()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_object('config.Config')

    # Initialize extensions
    mongo.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from .services.auth_service import auth_bp
    app.register_blueprint(auth_bp)

    return app