from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import test_app


db = SQLAlchemy(test_app)


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    url = db.Column(db.String(200))
    user_created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, email, url):
        self.username = username
        self.email = email
        self.url = url
        self.user_created_at = datetime.now()

    def __str__(self):
        return f'{self.username}'
