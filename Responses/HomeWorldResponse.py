from Responses.Response import Response


class HomeWorldResponse(Response):
    def __init__(self, address):
        super().__init__(address)

    def getData(self):
        responseData = super().getData()
        name = responseData["name"]
        return name
