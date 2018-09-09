import json
from flask import current_app as app
from flask import g
from flask import request
from flask_restplus import Resource
from flask_restplus import reqparse
from app.api.restplus_api import api
from app.api.models.entity_models import user
from common.security.token_validator import auth_required
from common.tojson import tojson

ns = api.namespace('user',  description='User registration and login')

@ns.route("/<string:username>")
class UsersMangement(Resource):

    @api.response(404, "User not found")
    @api.response(200, "User found")
    @auth_required
    @api.doc(security="apikey")
    def get(self, username):
        """
        Returns a user details
        """
        coll = g.contacts_book_db.rbac_users
        cursor = coll.find({"username": username})

        if cursor.count() < 1:
            return {"message": "user not registered {}".format(user)}, 400

        return tojson(cursor[0])


@api.response(500, "User registration failed")
@ns.route("/register")
class UsersMangement(Resource):
    @api.response(200, "User registered successfully")
    @api.response(400, "User already exist")
    @api.expect(user)
    def post(self):
        """
        Register a user
        """
        parser = reqparse.RequestParser()
        parser.add_argument("firstname", type=str, help='First Name', required=True)
        parser.add_argument("lastname", type=str, help="Last Name", required=True)
        parser.add_argument("username", type=str, help="Unique Username", required=True)
        parser.add_argument("password", type=str, help="Password", required=True)
        parser.add_argument("roles", type=str, help="Roles", action="append", required=True)
        request_obj = parser.parse_args(strict=True)

        coll = g.contacts_book_db.rbac_users
        cursor = coll.find({"username": request_obj["username"]})

        if cursor.count() >= 1:
            return {"message": "user already exist: {}".format(request_obj["username"])}, 400

        try:
            coll.insert_one(request_obj)
        except Exception as ex:
            app.logger.debug(ex)
            return 'could not save the request into mongodb', 500
        return tojson(request_obj), 200
