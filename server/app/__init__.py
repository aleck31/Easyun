from flask import Flask, render_template
from flask_admin import Admin
from app.view import init_view
from app import configs

# from flask_login import LoginManager
# from flask_mail import Mail

loginmanager = LoginManager()
loginmanager.session_protection = 'strong'
loginmanager.login_view = 'base.login'

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


class MyView(BaseView): 
    @expose('/') 
        def index(self):
            return self.render('admin/myindex.html') 
    @expose('/test/') 
        def test(self): 
            return self.render('admin/test.html') 

def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    loginmanager.init_app(app)

    from .base import base as base_blueprint
    app.register_blueprint(base_blueprint)
    return app
