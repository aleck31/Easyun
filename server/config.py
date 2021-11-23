import os

class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///base.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # openapi.info.description
    DESCRIPTION = '''
Easyun api docs:  
* Swagger docs path： /api/docs
* redoc path： /api/redoc'
    '''
    # openapi.servers
    SERVERS = [
        {
            'name': 'Development Server',
            'url': 'http://127.0.0.1:6660'
        },
        {
            'name': 'Testing Server',
            'url': 'http://54.156.105.123:6660'
        }
        ]
    
    # openapi.externalDocs
    EXTERNAL_DOCS = {
        'description': 'Find more info here',
        'url': 'https://boto3.amazonaws.com/v1/documentation/api/latest/guide/index.html'
        }


class TestConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
    FLASK_DEBUG = True
    SQLALCHEMY_ECHO = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    FLASK_DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    FLASK_DEBUG = False
    SQLALCHEMY_ECHO = False


env_config = {
    'test': TestConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
