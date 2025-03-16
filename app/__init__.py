from flask import Flask
from app.routes import register_routes
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    #Register API routes
    register_routes(app)

    return app
