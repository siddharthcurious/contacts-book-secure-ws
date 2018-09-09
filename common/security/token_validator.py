from functools import wraps
from flask import request
from flask import current_app as app
import base64


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return { "message": "Token is missing!" }, 403
        try:
            # jwt.decode(token, app.config["SECRET_KEY"])
            # jwt.decode(token, verify=False)
            # jwt.decode(token, base64.b64decode(), algorithms=['HS256'])
            token_data = token.split(".")
            data = base64.b64decode(token_data[1]+"==================================================================")
        except Exception  as ex:
            app.logger.debug(ex)
            app.logger.debug("Token validation error")
            return { "message": "Token is missing or invalid" }, 403
        return f(*args, **kwargs)
    return decorated

