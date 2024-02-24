import json
import os
from app.helpers.response import postRequest, internal_server_error


def createData(data):
    try:
        nim = data.get("nim")
        nama = data.get("nama")

        new_data = {"nim": nim, "nama": nama}

        current_script_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_script_path, '../models/data.json')

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