from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from .log import logger

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__)

    if environ.get('ENV') == 'PRODUCTION':
        app.config.from_object('config.ProductionConfig')
        logger.info("Loaded: Configuration of Production")
    else:
        app.config.from_object('config.DevelopmentConfig')
        logger.info("Loaded: configuration of Development")

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create database tables for our data models

        return app
