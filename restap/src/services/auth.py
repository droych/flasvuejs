from datetime import timedelta
from http import HTTPStatus

from flask_jwt_extended import jwt_required, get_jwt_identity, set_access_cookies, create_access_token, \
    unset_jwt_cookies

from src.common.base import app
from src.db.model import User
from src.schemas.user import users_schema,user_schema
from flask_restful import Resource,request
from src.db.model import db, User
from flask import make_response, jsonify

from src.decor.admindec import admin_required
from src.utils.bcrpt import encrypt_password,compare_passwords
from src.utils.jwttoken import generate_login_token, unset_login, refresh

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
class SignupResource(Resource):
    def post(self):
        try:
            new_User = User(
            username = request.json['username'],
            email = request.json['email'],
            phone_number = request.json['phone_number'],
            password = encrypt_password(request.json['password']),
            user_address = request.json['user_address']
                )
            db.session.add(new_User)
            db.session.commit()
            print(vars(new_User))
            return user_schema.dump(new_User)

        except Exception as e:
            print(e)
class LoginResource(Resource):
    try:
        def post(self):
            password = request.json['password']
            users = User.query.filter_by(email=request.json['email']).first()
            if not users:
                          return  HTTPStatus.BAD_REQUEST
            elif compare_passwords(password,users.password):
                        response =  generate_login_token(users.email)
                        resp = jsonify({'acess token': list(response.values())[0]})
                        #    print(list(token.values())[0])
                        set_access_cookies(resp, list(response.values())[0])
                        print(set_access_cookies(resp, list(response.values())[0]))
                        print(resp)
                        cookie_token = create_access_token(identity=users.email, expires_delta=timedelta(days=300))
                        print(vars(resp))
                        set_access_cookies(resp, cookie_token)

                        return resp

            else:
                return HTTPStatus.CONFLICT
    except Exception as e:
        print(e)

class LogoutResource(Resource):
    def post(self):
        response = {"msg": "logout successful"}
        unset_jwt_cookies(jsonify(response))
        return jsonify(response)


class Refresh(Resource):
    def get(self):
        return refresh(), HTTPStatus.OK

class UserListResource(Resource):
    def get(self):
        user = User.query.all()
        return users_schema.dump(user)


class UserResource(Resource):
    def get(self, id):
        user_select = User.query.get_or_404(id)
        return user_schema.dump(user_select)

    def put(self,id):
        user_update = User.query.get_or_404(id)

        _name = request.json['name'],
        _email = request.json['email'],
        _phone_number = request.json['phone_number'],
        _password = request.json['password']
        user_update.name = _name
        user_update.email = _email
        user_update.phone_number = _phone_number
        user_update.password = _password
        db.session.add( user_update)
        db.session.commit()
        return user_schema.dump(user_update)

    def patch(self, id):
        User = User.query.get_or_404(id)

        if 'User_name' in request.json:
            User.name = request.json['User_name']
        if 'User_rate' in request.json:
            User.content = request.json['User_rate']
        if 'quantity' in request.json:
            User.content = request.json['quantity']


        db.session.commit()
        return user_schema.dump(User)

    def delete(self, id):
        User = User.query.get_or_404(id)
        db.session.delete(User)
        db.session.commit()
        return '', 204

class Admin(Resource):
    @jwt_required()
    @admin_required([1])
    def post(self,**kwargs):
        try:

            current_user = get_jwt_identity()
            # user = User.query.filter_by(login=name).first_or_404(description="User not found")

            print(current_user)
            return current_user
        except Exception as e:
            return {'error': str(e)}
