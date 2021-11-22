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
# from flask_migrate import Migrate


# define api version
ver = '/api/v1.0'

# db variable initialization
db = SQLAlchemy()

def create_app():
    app = APIFlask(__name__, docs_path='/api/docs', redoc_path='/api/redoc')

    # openapi.info.description
    app.config['DESCRIPTION'] = '''
Easyun api docs:  
* Swagger docs path： /api/docs
* redoc path： /api/redoc'
```
//Start application
$ python run.py
or
$ flask run
```
    '''

    # openapi.servers
    app.config['SERVERS'] = [
        {
            'name': 'Development Server',
            'url': 'http://127.0.0.1:660'
        },
        {
            'name': 'Testing Server',
            'url': 'http://54.156.105.123:660'
        }
        ]

    # openapi.externalDocs
    app.config['EXTERNAL_DOCS'] = {
        'description': 'Find more info here',
        'url': 'https://boto3.amazonaws.com/v1/documentation/api/latest/guide/index.html'
        }

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///easyun.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    # migrate = Migrate(app, db, compare_type=True)

    @app.before_first_request
    def init_database():
        db.create_all()

    # 导入各模块blueprint；
    from .common import auth
    from .modules import mserver

    # 注册blueprint
    app.register_blueprint(auth.bp)
    app.register_blueprint(mserver.bp)

    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler(
            'logs/easyun_api.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    # if config_name != 'test':
    #     app.logger.info('Easyun API startup')

    return app