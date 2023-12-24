from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    hashed_password = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    statisitcs = db.relationship('Statistics', back_populates='owner', uselist = True,
                              cascade = 'all, delete-orphan, delete')

class Statistics(db.Model):
    __tablename__ = 'stats'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    results = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    owner = db.relationship('User', back_populates='statistics')