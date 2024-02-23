from flask import Flask
from app.routes import main_api


app = Flask(__name__)

app.register_blueprint(main_api.Main)


