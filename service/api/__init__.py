from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ, sys
from .log import accesslogger
import logging

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)

    """Loading configuratons."""
    if environ.get('ENV') == 'PRODUCTION':
        app.config.from_object('config.ProductionConfig')
        accesslogger.info("Loaded: Configuration of Production")
    elif environ.get('ENV') == 'STAGE':
        app.config.from_object('config.StageConfig')
        accesslogger.info("Loaded: Configuration of Stage")
    elif environ.get('ENV') == 'TESTING':
        app.config.from_object('config.TestConfig')
        accesslogger.info("Loaded: Configuration of Testing")
    else:
        app.config.from_object('config.DevelopmentConfig')
        accesslogger.info("Loaded: configuration of Development")

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create database tables for our data models

        return app

authapp = create_app()
