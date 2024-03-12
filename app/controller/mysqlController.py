from app import db
from app.models.dmsModels import dms
from flask import request
from app.helpers.response import postRequest, bad_request

# Membuat produk
def create(data):
    try:
        send = data.get("send")

        sendData = {"send": send}

        post = dms(**sendData)

        db.session.add(post)
        db.session.commit()

        return postRequest(post)
        
    except Exception as e:
        print(e)
        return bad_request(e)
