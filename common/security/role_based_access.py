from functools import wraps
from flask import g
from flask import request
from flask import current_app as app
from bson.objectid import ObjectId
import base64
import json

def get_user_from_request():
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"]
    if not token:
        return {"message": "Token is missing!"}, 403
    try:
        # payload = jwt.decode(token, app.config["SECRET_KEY"])
        # return payload["user"]
        token_data = token.split(".")
        data = base64.b64decode(token_data[1]+"===========================================================================================================")
        return json.loads(data)["mudId"]
    except Exception as ex:
            app.logger.debug(ex)
            app.logger.debug("Token validation error")
    return None

def get_current_user_roles():
    if get_user_from_request():
        mud_id = get_user_from_request()
        coll = g.portaldb.rbac_users
        cursor = coll.find_one({"mudId": mud_id})
        # app.logger.debug(cursor)
        roles = []
        if cursor:
            role_id = None
            if isinstance(cursor["roleId"], list):
                role_id = cursor["roleId"][0]
            if isinstance(cursor["roleId"], str):
                role_id = cursor["roleId"]
            if role_id == None:
                app.logger.debug("Issue in finding role id and user id")
                return None
            ccoll = g.portaldb.rbac_roles
            ccursor = ccoll.find_one({"_id": ObjectId(role_id)})
            if ccursor:
                """
                Role and permissions are suppressed to method used by older version
                Admin, User
                It need to be incorporated with UI and other service.
                Example
                Admin - Can access all the APIs endpoints
                User - Can access only restricted APIs endpoints
                """
                permissions = ccursor["permissions"]["ENOD"]
                permissions_given = set(permissions)
                p_admin = ["CREATE", "VIEW", "UPDATE", "DELETE"]
                p_user = ["CREATE_AS_USER", "VIEW_AS_USER", "UPDATE_AS_USER"]

                permissions_admin = set(p_admin)
                if permissions_admin.issubset(permissions_given):
                    roles.append("admin")
                    return roles
                else:
                    permissions_user = set(p_user)
                    if permissions_user.issubset(permissions_given):
                        roles.append("user")
                    return roles
        else:
            return None

def is_roles_defined(roles_api):
    roles_db = get_current_user_roles()
    if roles_db is None:
        app.logger.debug("role not defined")
        return False
    roles_db_1 = set([x.lower() for x in roles_db])
    roles_api_1 = set([x.lower() for x in roles_api])
    if roles_db_1.issubset(roles_api_1):
        return True
    return False

def required_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not is_roles_defined(roles):
                return {"message": "You have no admin privilege to acomplish this task, Please contact RDIP portal admin"}, 201
            return f(*args, **kwargs)
        return wrapped
    return wrapper

