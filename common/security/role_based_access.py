from functools import wraps
from flask import g
from flask import request
from flask import current_app as app
import jwt

def get_user_from_request():
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"]
    if not token:
        return {"message": "Token is missing!"}, 403
    try:
        payload = jwt.decode(token, app.config["SECRET_KEY"])
        return payload["username"]
    except Exception as ex:
            app.logger.debug(ex)
            app.logger.debug("Token validation error")
    return None

def get_current_user_roles():
    if get_user_from_request():
        user = get_user_from_request()
        coll = g.contacts_book_db.rbac_users
        cursor = coll.find_one({"username": user})
        if cursor:
            return cursor["roles"]
        else:
            return None

def is_roles_defined(roles_api):
    roles_db = get_current_user_roles()
    if roles_db is None:
        app.logger.debug("role not defined")
        return False
    roles_from_api = set(roles_api)
    app.logger.debug(roles_from_api)
    roles_from_db = set(roles_db)
    app.logger.debug(roles_from_db)
    if roles_from_db.issubset(roles_from_api):
        return True
    return False

def required_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not is_roles_defined(roles):
                return {"message": "You have no admin privilege to acomplish this task, Please admin"}, 201
            return f(*args, **kwargs)
        return wrapped
    return wrapper

