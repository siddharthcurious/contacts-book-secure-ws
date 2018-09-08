import json
from bson import json_util
from flask import current_app as app
from flask import g
from flask import request
from flask_restplus import Resource
from flask_restplus import reqparse
from app.api.restplus_api import api
from app.api.models.entity_models import person

ns = api.namespace('persons',  description='Operations - Contacts')

def tojson(object):
    if object:
        return json.loads(json_util.dumps(object))
    else:
        return None

@ns.route("/contact/create")
@api.response(404, "Contact not found")
class Person(Resource):

    @api.response(200, "Successfully created contact")
    @api.response(400, "Contact already exist")
    @api.expect(person)
    def post(self):
        """
        Create contact of a person
        """
        parser = reqparse.RequestParser()
        parser.add_argument("firstname", type=str, help='First Name', required=True)
        parser.add_argument("lastname", type=str, help="Last Name", required=True)
        parser.add_argument("emailid", type=str, help="Email Id", required=True)
        parser.add_argument("phone", type=str, help="Phone Number", action="append", required=True)
        request_obj = parser.parse_args(strict=True)

        coll = g.contacts_book_db.contacts
        cursor = coll.find({"emailid": request_obj["emailid"]})

        if cursor.count() >= 1:
            return {"message":"user already exist"}, 400

        try:
            coll.insert_one(request_obj)
        except Exception as ex:
            app.logger.debug(ex)
            return 'could not save the request into mongodb', 500
        return tojson(request_obj), 200

@ns.route("/contact/<string:emailid>")
@api.response(404, "Contact not found")
class Person(Resource):

    @api.response(200, "Successfully updated contact")
    @api.response(500, "Contact could not updated")
    @api.expect(person)
    def put(self, emailid):
        """
        Update contact of a person
        """
        parser = reqparse.RequestParser()
        parser.add_argument("firstname", type=str, help='First Name', required=True)
        parser.add_argument("lastname", type=str, help="Last Name", required=True)
        parser.add_argument("emailid", type=str, help="Email Id", required=True)
        parser.add_argument("phone", type=str, help="Phone Number", action="append", required=True)
        request_obj = parser.parse_args(strict=True)

        coll = g.contacts_book_db.contacts
        contact_request = coll.find_one({"emailid": emailid})

        if not contact_request:
            return {"message": "{} not found".format(emailid)}, 404

        contact_request.update(request_obj)
        try:
            coll.save(contact_request)
        except Exception as ex:
            app.logger.debug(ex)
            return 'could not save the request into mongodb', 500
        return tojson(contact_request), 200

@ns.route("/search/<string:emailid>")
class Person(Resource):
    @api.response(200, "Contact found")
    @api.response(404, "Contact not found")
    def get(self, emailid):
        """
        Get contact by email id
        """
        coll = g.contacts_book_db.contacts
        cursor = coll.find({"emailid": emailid})
        if cursor.count() == 0:
            return {"message": "not found"}, 404
        return tojson(cursor[0]), 200

@ns.route("/search/firstname/<string:firstname>")
class Person(Resource):
    @api.response(200, "Contacts found")
    @api.response(404, "Contacts not found")
    def get(self, firstname):
        """
        Get contacts by firstname
        """
        coll = g.contacts_book_db.contacts
        cursor = coll.find({"firstname": firstname})
        if cursor.count() == 0:
            return {"message": "not found"}, 404
        return tojson(cursor), 200

@ns.route("/search/lastname/<string:lastname>")
class Person(Resource):
    @api.response(200, "Contacts found")
    @api.response(404, "Contacts not found")
    def get(self, lastname):
        """
        Get contacts by lastname
        """
        coll = g.contacts_book_db.contacts
        cursor = coll.find({"lastname": lastname})
        if cursor.count() == 0:
            return {"message": "not found"}, 404
        return tojson(cursor), 200

@ns.route("/contacts")
class Person(Resource):
    @api.response(200, "Contacts found")
    @api.response(404, "Contacts not found")
    def get(self):
        """
        Get all contacts
        """
        coll = g.contacts_book_db.contacts
        cursor = coll.find()
        if cursor.count() == 0:
            return {"message": "not found"}, 404
        return tojson(cursor), 200

@ns.route("/<string:firstname>")
class Person(Resource):
    @api.response(200, "Contacts found")
    @api.response(404, "Contacts not found")
    def get(self, firstname):
        """
        Search contacts by first name and default pagesize is 10
        """
        dps = 10

        print "hello"

        coll = g.contacts_book_db.contacts
        cursor = coll.find({"firstname": firstname})

        if cursor.count() == 0:
            return {"message": "not found"}, 404

        if cursor.count() >= 10:
            return tojson(cursor[10])
        else:
            return tojson(cursor), 200

@ns.route("/search/<string:firstname>/<int:pagenum>/<int:pagesize>")
class Person(Resource):
    @api.response(200, "Contacts found")
    @api.response(404, "Contacts not found")
    def get(self, firstname, pagenum, pagesize):
        """
        Search contacts by firstname and pagination
        """

        if pagenum <= 0 or pagesize <= 0:
            return {"message": "negative value not allowed"}, 404

        coll = g.contacts_book_db.contacts
        cursor = coll.find({"firstname": firstname})

        if cursor.count() == 0:
            return {"message": "not found"}, 404

        datalen = cursor.count()

        start = (pagenum-1)*pagesize
        end = pagenum*(pagesize)

        if start < end <= datalen:
            return tojson(cursor[start:end])
        elif end > datalen:
            return tojson(cursor[start:datalen])

        return tojson(cursor), 200





