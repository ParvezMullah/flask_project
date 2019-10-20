from flask_marshmallow import Marshmallow 
from marshmallow import Schema, fields, validate
from app import test_app
from models import UserModel
ma = Marshmallow(test_app)

class UserSchema(ma.Schema):
    username = fields.Str(validate=validate.Length(max=80, min=3,), error="username shall be 3 to 80 characters", required=True)
    email = fields.Str(required=True)
    url = fields.URL(required=True)