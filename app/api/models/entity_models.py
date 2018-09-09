from flask_restplus import fields
from app.api.restplus_api import api

person = api.model("Person", {
    "firstname": fields.String,
    "lastname": fields.String,
    "emailid": fields.String,
    "phone": fields.List(fields.String)
})

user = api.model("User", {
    "firstname": fields.String,
    "lastname": fields.String,
    "username": fields.String,
    "password": fields.String,
    "roles": fields.List(fields.String)
})