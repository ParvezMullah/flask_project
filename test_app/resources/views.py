from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError
from schema import UserSchema
from models import UserModel, db

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class User(Resource):
    def post(self):
        try:
            user_input = dict(request.args)
            validated_input = user_schema.load(user_input)
            user = UserModel(user_input['username'],
                             user_input['email'], user_input['url'])
            db.session.add(user)
            db.session.commit()
            return {'message': "User created successfully"}
        except ValidationError as e:
            return {'messsage': e.messages}, 400
        except Exception as e:
            return {'message': str(e)}, 400

    def get(self):
        try:
            all_users = UserModel.query.all()
            all_users = users_schema.dump(all_users)
            return {"message": all_users}
        except Exception as e:
            return {"message": str(e)}, 400

    def put(self):
        pass

    def delete(self):
        pass
