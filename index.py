import os
from flask import g
import argparse
import json
from mongodb_util import Util
from flask import Flask
from flask_cors import CORS
from app.api.restplus_api import api
from flask_restplus import abort
from app.api.resources.contacts_controller import ns as contacts_namespace
from app.api.resources.users_controller import ns as users_namespace
from app.api.resources.token_generator import ns as toke_namespace
from app.api.resources.populate_data import ns as populate_data

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

configs = {
    "dev"  	: "app.config.DevConfig",
    "prod" 	: "app.config.ProdConfig",
    "test"  : "app.config.TestConfig",
    "local" : "app.config.LocalConfig"
}

parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host", default="0.0.0.0", help="hostname for application [127.0.0.1]", type=str)
parser.add_argument("-P", "--port", default=5000, help="port number for the application [int type]", type=int)
parser.add_argument("-E", "--env", default="local", help="deployment environment [local|dev|test|prod]", type=str)
parser.add_argument("-C", "--cfg", default="file", help="Overriding config source [db|http|file]", type=str)
args = parser.parse_args()

app.config.from_object(configs[args.env])

if args.cfg == "http":
    pass
if args.cfg == "db":
    print "San"
if args.cfg == "file":
    with open("properties/configuration.json") as config_obj:
        config_json = json.load(config_obj)
        config_env = config_json[args.env.upper()]
        config_keys = config_env.keys()
        for key in config_keys:
            app.config[key] = config_env[key]

@app.route("/")
def hello():
    return "Hello User"

"""
util = Util()
@app.before_request
def database_object():
    app.logger.debug(id(util))
    contacts_book_db = util.get_mongodb()
    if contacts_book_db:
        g.contacts_book_db = contacts_book_db
    else:
        abort(500, custom='mongodb connection refused')
"""

api.init_app(app=app)
api.add_namespace(contacts_namespace)
api.add_namespace(users_namespace)
api.add_namespace(toke_namespace)
api.add_namespace(populate_data)

if __name__ == "__main__":

    port = int(os.environ.get('PORT', args.port))
    app.run(debug=True, host=args.host, port=port)
