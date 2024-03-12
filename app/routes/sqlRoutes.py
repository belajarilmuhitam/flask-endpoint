from flask import Blueprint,request
from app.helpers.response import getRequest, internal_server_error
from app.controller import mysqlController

Send = Blueprint('send', __name__, template_folder='..template')

# @Main.route('/', methods=["GET"])
# def index():
#     return getRequest(data=None)

@Send.route('/post', methods=["POST"])
def post():
    try:

        return mysqlController.create()

    except Exception as e:

        return internal_server_error(str(e))
    