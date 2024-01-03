from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
login_manager = LoginManager()
DB_NAME = "database.db"

def create_app():
    BASE_DIR = path.abspath(path.dirname(__file__))
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Super secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(BASE_DIR, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app);
    
    from .views import views
    from .auth import auth

    # Initialize the login manager
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')

    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all() 

    return app