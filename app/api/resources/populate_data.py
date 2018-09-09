from flask_restplus import Resource
from flask import current_app as app
from app.api.restplus_api import api
from flask import g
from common.tojson import tojson
from flask_restplus import cors

ns = api.namespace('populate',  description='For testing purpose, populate data to mongodb')

@api.response(500, "Could not populate data")
@ns.route("/data")
class PopulateData(Resource):

    @cors.crossdomain(origin='*')
    def get(self):

        data = [
            {"firstname": "harish", "lastname": "singh", "emailid": "harish@gmail.com", "phone": "+91-789087977"},
            {"firstname": "ram", "lastname": "singh", "emailid": "r@gmail.com", "phone": "+91-789087977"}
        ]

        coll = g.contacts_book_db.contacts
        coll.drop()

        try:
            coll.insert_many(data)
        except Exception as ex:
            app.logger.debug(ex)
            return 'could not save the request into mongodb', 500
        return tojson(data), 200