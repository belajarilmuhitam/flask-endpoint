import os

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigSQL: 
    HOST = str(os.environ.get("SQL_DB_HOST"))
    DATABASE = str(os.environ.get("SQL_DB_DATABASE"))
    PORT = os.environ.get("DB_PORT", "3306")
    USERNAME = str(os.environ.get("SQL_DB_USERNAME"))
    PASSWORD = str(os.environ.get("SQL_DB_PASSWORD"))

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
