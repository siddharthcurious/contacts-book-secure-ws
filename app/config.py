import os

class BaseConfig(object):
    DEBUG = False

class LocalConfig(BaseConfig):
    MONGO_URI = 'mongodb://localhost:27017'
    MONGO_DATABASE = 'contacts_book'
    SSLFLAG = False
    SSLCERT = None

class DevConfig(BaseConfig):
    pass

class TestConfig(BaseConfig):
    pass

class ProdConfig(BaseConfig):
    pass

