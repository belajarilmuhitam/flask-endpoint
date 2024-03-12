from flask import Blueprint,request
from app.helpers.response import getRequest, internal_server_error
from app.controller.jsonController import createData

Main = Blueprint('main', __name__, template_folder='..template')

@Main.route('/', methods=["GET"])
def index():
    return getRequest(data=None)

@Main.route('/', methods=["POST"])
def post():
    try:
        input_data = request.get_json()

        createData_result = createData(input_data)

        return createData_result
    except Exception as e:

        return internal_server_error(str(e))
    