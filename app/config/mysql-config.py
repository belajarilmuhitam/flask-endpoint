import os

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigSQL: 
    HOST = str(os.environ.get("SQL_DB_HOST"))
    DATABASE = str(os.environ.get("SQL_DB_DATABASE"))
    USERNAME = str(os.environ.get("SQL_DB_USERNAME"))
    PASSWORD = str(os.environ.get("SQL_DB_PASSWORD"))

    SQLALCHEMY_DATABASE_URI = 'mysql+pymsql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
