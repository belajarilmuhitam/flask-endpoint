import json
import os
from app.helpers.response import postRequest, internal_server_error, bad_request
from datetime import datetime


def createData(data):
    try:
        nim = data.get("nim")
        nama = data.get("nama")
        timestamp = datetime.now().isoformat()

        new_data = {"nim": nim, "nama": nama, "timestamp": timestamp}

        current_script_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_script_path, '../models/data.json')

        if nim is None or nama is None:
            return bad_request()
        else:
            existing_data = []
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                with open(file_path, 'r') as file:
                    existing_data = json.load(file)

            if not isinstance(existing_data, list):
                existing_data = []

            existing_data.append(new_data)

            with open(file_path, 'w') as file:
                json.dump(existing_data, file, indent=2)

            return postRequest(new_data)
                     
    except Exception as e:
        return internal_server_error(str(e))