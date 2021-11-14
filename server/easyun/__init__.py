from flask import Flask, jsonify, request

# from flask_admin import Admin
# from app.view import init_view
# from app import configs
# from flask_login import LoginManager
# from flask_mail import Mail

# loginmanager = LoginManager()
# loginmanager.session_protection = 'strong'
# loginmanager.login_view = 'base.login'

# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
# db = SQLAlchemy()

app = Flask(__name__)
app.app_context()

msg= [
    {'Name':'Easyun',
    'status':'ok'}
    ]

@app.route('/easyun', methods=['GET'])
def create_app(config_name=None):    
    return jsonify(msg)