from Responses.Response import Response


class NumberOfHumanResponse(Response):
    def __init__(self, address):
        super().__init__(address)

    def getData(self):
        responseData = super().getData()
        numberOfHumans = responseData["count"]
        return numberOfHumans

