from flask_restplus import Resource
from flask import current_app as app
from app.api.restplus_api import api
import jwt
import datetime
from flask_restplus import cors

"""
This is API is developed to test JWT token, we may not use in production environment.
"""

ns = api.namespace('testing',  description='For testing security, generate JWT token')

@api.response(500, "Could not generate token")
@ns.route("/generate/<string:user>")
class TokenTesting(Resource):
	@cors.crossdomain(origin='*')
	@api.response(200, "Successfully generated token")
	def get(self, user, *args, **kwargs):
		token = jwt.encode({"user": user, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, app.config["SECRET_KEY"])
		return {"token": token}, 200
