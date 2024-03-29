from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import enum

class Activities(enum.Enum):
    reaction_time = 1
    sequence_memory = 2
    word_generation = 3
    matching_colors = 4
    pattern_memory = 5
    quick_calculus = 6
    aim_training = 7
    fast_typing = 8

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    hashed_password = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    statistics = db.relationship('Statistics', back_populates='owner', uselist = True,
                              cascade = 'all, delete-orphan, delete', lazy='dynamic')

class Statistics(db.Model):
    __tablename__ = 'stats'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.Enum(Activities), nullable=False)
    results = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    owner = db.relationship('User', back_populates='statistics')