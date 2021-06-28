from Models.Human import Human
from Responses.HomeWorldResponse import HomeWorldResponse
from Responses.Response import Response
from Responses.StarShipResponse import StarShipResponse


class HumanResponse(Response):
    def __init__(self, address):
        super().__init__(address)

    def getData(self):
        responseData = super().getData()
        name = responseData["name"]
        height = responseData["height"]
        gender = responseData["gender"]
        homeWorldAddress = responseData["homeworld"]
        homeWorldResponse = HomeWorldResponse(homeWorldAddress)
        homeWorldResponseData = homeWorldResponse.getData()
        homeWorldName = homeWorldResponseData
        starShips = []
        starsShipsAddresses = responseData["starships"]
        for starShipAddress in starsShipsAddresses:
            starShipResponse = StarShipResponse(starShipAddress)
            starShip = starShipResponse.getData()
            starShips.append(starShip)
        human = Human(name, homeWorldName, height, gender, starShips)
        return human

