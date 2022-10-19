from flask_jwt_extended import create_access_token, \
    get_jwt_identity, \
    jwt_required, JWTManager, create_refresh_token, unset_jwt_cookies

from src.common.base import app
import bcrypt
from datetime import timedelta
from flask import jsonify
jwt = JWTManager(app)
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_SECRET_KEY"] = "idkwthmid"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=30)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True

def generate_login_token(user_name):
    access_token = create_access_token(identity=user_name)
    refresh_token = create_refresh_token(identity=user_name)
    response = {
        'access_token': access_token,
        'refresh_token': refresh_token

    }

    return response


def unset_login():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

@jwt_required(refresh=True)
def refresh():
        identity = get_jwt_identity()
        print(identity)
        access_token = create_access_token(identity=identity)
        return {'access_token': access_token}