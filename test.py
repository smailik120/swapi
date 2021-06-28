from Responses.PeopleResponse import PeopleResponse
from config.config import peopleAddress
peopleAddress = peopleAddress
response = PeopleResponse(peopleAddress)
data = response.getData()