from pymongo import MongoClient
from pymongo import errors
from flask import current_app as app
from common.singleton_decorator import singleton
from flask_restplus import abort

@singleton
class Util:
    def connect(self, MONGO_URI, SSLFLAG=False, SSLCERT=None):
        if SSLFLAG == True:
            mongo_client = MongoClient(MONGO_URI, ssl=SSLFLAG, ssl_ca_certs=SSLCERT)
        else:
            mongo_client = MongoClient(MONGO_URI)

        try:
            mongo_client.server_info()
        except errors.ServerSelectionTimeoutError as e:
            app.logger.error("mongodb connection problem %s.", MONGO_URI)
            mongo_client = None
        return mongo_client

    def get_mongodb(self):
        mongodb_connect = self.connect(app.config['MONGO_URI'], app.config['SSLFLAG'], app.config['SSLCERT'])
        if mongodb_connect:
            contacts_book_db = mongodb_connect[app.config['MONGO_DATABASE']]
            return contacts_book_db







