import jdxapi.config
import os
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from jdxapi.utils.error import ApiError
from flask_cors import CORS

def configure_app(app):
    database_uri = os.getenv('SQLALCHEMY_DATABASE_URI')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    # Maximum uploaded file size is 16 MB
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    app.config['SQLALCHEMY_ECHO'] = False


    # if os.getenv('ENV') == 'DEV' :
    # if os.getenv('ENV') in ['DEV', 'TEST'] :
    #     app.config['SQLALCHEMY_ECHO'] = False
    return app


def create_app():
    app = Flask(__name__)
    app = configure_app(app)

    @app.errorhandler(ApiError)
    def handle_api_error(error):
        return error.get_response()

    return app



import logging
from logging import handlers

def create_logger():
    logger = logging.getLogger('inputoutput')
    logger.setLevel(logging.INFO)
    log_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s') # %(name)s gives you the logger name
    rotating_handler = handlers.TimedRotatingFileHandler("/logs/jdxapi.log", 'D', 1, 10)
    rotating_handler.setLevel(logging.INFO)
    rotating_handler.setFormatter(log_formatter)
    logger.addHandler(rotating_handler)

create_logger()



app = create_app()
CORS(app)
api = Api(app)
DB = SQLAlchemy(app)

# TODO autopep8 will move the imports for 
# routes and models up but they must be here
# after the api and DB are created
from jdxapi.routes import *
from jdxapi.models import *

DB.drop_all()
DB.create_all()
DB.session.commit()

from jdxapi.models.scripts import populate_db
