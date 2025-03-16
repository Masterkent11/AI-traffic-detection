from flask import Blueprint
from app.routes.detection_routes import detection_bp

def register_routes(app):
    app.register_blueprint(detection_bp, url_prefix='/api')