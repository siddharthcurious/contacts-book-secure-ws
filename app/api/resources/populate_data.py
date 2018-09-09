from flask_restplus import Resource
from flask import current_app as app
from app.api.restplus_api import api
from flask import g

ns = api.namespace('populate',  description='For testing purpose, populate data to mongodb')

@api.response(500, "Could not populate data")
@ns.route("/data")
class PopulateData(Resource):

    def get(self):

        data = [
            {"firstname": "ram",    "lastname": "singh", "emailid": "a@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "yadav", "emailid": "b@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "gond",  "emailid": "c@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "kumar", "emailid": "d@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "kumar", "emailid": "e@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "f@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "g@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "h@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "i@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "j@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "k@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "l@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "m@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "n@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "o@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "p@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "q@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "r@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "shyam",  "lastname": "singh", "emailid": "abc@gmail.com", "phone": "+91-789087977"},
            {"firstname": "shyam",  "lastname": "saxena", "emailid": "xyg@gmail.com", "phone": "+91-789087977"},
            {"firstname": "shyam",  "lastname": "dude", "emailid": "har@gmail.com", "phone": "+91-789087977"},
            {"firstname": "shyam",  "lastname": "singh", "emailid": "shy@gmail.com", "phone": "+91-789087977"}
        ]

        coll = g.contacts_book_db.contacts
        coll.drop()

        try:
            coll.insert_many(data)
        except Exception as ex:
            app.logger.debug(ex)
            return 'could not save the request into mongodb', 500

        coll = g.contacts_book_db.rbac_users
        coll.drop()

        data = [
            {"firstname": "harish",  "lastname": "singh", "username": "harish",  "password": "harish",  "roles": ["ADMIN", "USER"]},
            {"firstname": "ram",     "lastname": "gond",  "username": "ram",     "password": "ram",     "roles": ["ADMIN"]},
            {"firstname": "mohan",   "lastname": "yadav", "username": "mohan",   "password": "mohan",   "roles": ["ADMIN"]},
            {"firstname": "sanjeev", "lastname": "kumar", "username": "sanjeev", "password": "sanjeev", "roles": ["USER"]},
            {"firstname": "john",    "lastname": "singh", "username": "john",    "password": "john",    "roles": ["USER"]}
        ]

        try:
            coll.insert_many(data)
        except Exception as ex:
            app.logger.debug(ex)
            return 'could not save the request into mongodb', 500

        return "Successfully uploaded data", 200