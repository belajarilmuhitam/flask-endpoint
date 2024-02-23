from flask import request
from app.helpers.response import postRequest

def createData():
    try:
        nim = request.form.get("nim")
        nama = request.form.get("nama")

        
                     
    except Exception as e:
        # Handle exceptions, log them, or return an appropriate response
        pass
