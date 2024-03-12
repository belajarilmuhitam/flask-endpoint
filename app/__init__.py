from flask import Flask
from app.routes import jsonRoutes
from app.routes import sqlRoutes
from app.config.mysql import ConfigSQL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(ConfigSQL)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models.dmsModels import dms
app.register_blueprint(jsonRoutes.Main)
app.register_blueprint(sqlRoutes.Send)