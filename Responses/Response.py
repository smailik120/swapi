from Requests.JsonRequest import JsonRequest


class Response:
    def __init__(self, address):
        self.address = address

    def getData(self):
        request = JsonRequest(self.address)
        responseData = request.getData()
        return responseData