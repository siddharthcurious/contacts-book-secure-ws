import json
from flask import current_app as app
from flask import g
from flask import request
from flask_restplus import Resource
from flask_restplus import reqparse
from app.api.restplus_api import api
from app.api.models.entity_models import user
from flask_restplus import cors

ns = api.namespace('users',  description='User registration and login')

@ns.route("/<string:username>")
class PersonaTools(Resource):

    @api.response(404, "User not found")
    @api.response(200, "User found")
    @cors.crossdomain(origin='*')
    def get(self, username):
        """
        Returns a persona details
        """
        return {"hey": "man"}, 200

    @cors.crossdomain(origin='*')
    @api.response(200, "User created successfully")
    @api.response(500, "User registration failed")
    @api.expect(user)
    def post(self):
        """
        Creates an edge node on request
        """
        pass