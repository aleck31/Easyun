# -*- coding: UTF-8 -*-
'''
@Description: The app module, containing the app factory function.
@LastEditors: 
'''
import os
import logging
from apiflask import APIFlask
from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from config import env_config
from flask_migrate import Migrate


# define api version
ver = '/api/v1.0'

# db variable initialization
db = SQLAlchemy()

def create_app(run_env):
    app = APIFlask(__name__, docs_path='/api/docs', redoc_path='/api/redoc') 
    app.config.from_object(env_config[run_env])

    db.init_app(app)

    @app.before_first_request
    def init_database():
        db.create_all()
        return None

    migrate = Migrate(app, db, compare_type=True)

    register_blueprints(app)
    configure_logger(app)

    app.logger.setLevel(logging.INFO)
    if run_env != 'test':
        app.logger.info('Easyun API Start')

    return app


# 注册 Flask blueprints
def register_blueprints(app):
    """Register Flask blueprints."""
    from .common import auth
    # from .modules import mserver

    app.register_blueprint(auth.bp)
    # app.register_blueprint(mserver.bp)
    return None

def configure_logger(app):
    """Configure loggers."""
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler(
            'logs/easyun_api.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        if not app.logger.handlers:
            app.logger.addHandler(file_handler)    