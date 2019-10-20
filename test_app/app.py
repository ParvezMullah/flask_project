from flask import Flask
from flask_restful import Api
import os

test_app = Flask(__name__)
api = Api(test_app)

from resources.views import User


api.add_resource(User, '/')

basedir = os.path.abspath(os.path.dirname(__file__))

test_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
test_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run