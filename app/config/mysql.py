import os

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigSQL: 
    HOST = os.environ.get("DB_HOST", "localhost")
    DATABASE = os.environ.get("DB_NAME", "cobalagi")
    USERNAME = os.environ.get("DB_USER", "root")
    PASSWORD = os.environ.get("DB_PASSWORD", "")

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://" + USERNAME + ":" + PASSWORD + "@" + HOST + "/" + DATABASE
    )    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True