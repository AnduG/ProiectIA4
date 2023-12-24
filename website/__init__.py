from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    BASE_DIR = path.abspath(path.dirname(__file__))
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Super secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(BASE_DIR, 'myapp.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app);

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')

    from .models import User, Statistics

    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()

    return app