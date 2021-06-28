import requests
import json
from Exceptions.CodeException import CodeException
from Requests.Request import Request


class JsonRequest(Request):
    def __init__(self, address):
        super().__init__(address)

    def getData(self):
        response = requests.get(self.address)
        if response.status_code == 200:
            jsonData = json.loads(response.text)
            return jsonData
        else:
            raise CodeException()
