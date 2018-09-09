from flask_restplus import Resource
from flask import current_app as app
from app.api.restplus_api import api
import jwt
import datetime
from flask import g

"""
This is API is developed to test JWT token, we may not use in production environment.
"""

ns = api.namespace('testing',  description='For testing security, generate JWT token')

@api.response(500, "Could not generate token")
@api.response(404, "User not registered")
@ns.route("/generate/<string:username>/<string:password>")
class TokenTesting(Resource):
    @api.response(200, "Successfully generated token")
    def get(self, username, password, *args, **kwargs):

        coll = g.contacts_book_db.rbac_users
        cursor = coll.find({"username": username, "password": password})

        if cursor.count() < 1:
            return "user not registered, please register", 404

        token = jwt.encode({
                "username": username, "password": password,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
                app.config["SECRET_KEY"], algorithm='HS256')

        return {"token": token}, 200
