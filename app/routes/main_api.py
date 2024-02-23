from flask import jsonify, Blueprint,request
from app.controller import main_controller
from app.helpers.response import getRequest, postRequest

Main = Blueprint('main', __name__, template_folder='..template')

@Main.route('/', methods=["GET"])
def index():
    return getRequest(data=None)

@Main.route('/', methods=["POST"])
def post():
    input_data = request.get_json()
    return postRequest(input_data)

