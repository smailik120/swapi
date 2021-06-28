from Models.StarShip import StarShip
from Responses.Response import Response


class StarShipResponse(Response):
    def __init__(self, address):
        super().__init__(address)

    def getData(self):
        responseData = super().getData()
        name = responseData["name"]
        starShip = StarShip(name)
        return starShip

