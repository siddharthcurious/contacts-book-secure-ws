from functools import wraps
from flask import request
from flask import current_app as app
import jwt
from flask import current_app as app

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return { "message": "Token is missing!" }, 403
        try:
            jwt.decode(token, app.config["SECRET_KEY"], algorithms=['HS256'])
        except Exception  as ex:
            app.logger.debug(ex)
            app.logger.debug("Token validation error")
            return { "message": "Token is missing or invalid" }, 403
        return f(*args, **kwargs)
    return decorated

