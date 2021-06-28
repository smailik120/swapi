from Database.MysqlDriver import MysqlDriver
from Responses.HumanResponse import HumanResponse
from Responses.NumberOfHumanResponse import NumberOfHumanResponse
from Responses.Response import Response
from Transformers.DataFrameTransformer.PeopleTransformer import PeopleTransformer
from config.config import path_to_people_csv_file, mysqlConfig


class PeopleResponse(Response):
    def __init__(self, address):
        super().__init__(address)
    def getData(self):
        records = []
        numberOfHumanResponse = NumberOfHumanResponse(self.address)
        numberOfHumans = numberOfHumanResponse.getData()
        peopleCounter = 0
        humans = []
        currentNumberOfHuman = 1
        while peopleCounter != numberOfHumans:
            try:
                humanResponse = HumanResponse(self.address + f"/{currentNumberOfHuman}")
                human = humanResponse.getData()
                humans.append(human)
                peopleCounter += 1
            except:
                pass
            finally:
                currentNumberOfHuman += 1
        for human in humans:
            humanRecords = human.getHumanRecords()
            records.extend(humanRecords)
        dataFrame = PeopleTransformer(records).transform()
        dataFrame.to_csv(path_to_people_csv_file, index=False)
        mysqlDriver = MysqlDriver(mysqlConfig.login, mysqlConfig.password, mysqlConfig.hostName, mysqlConfig.port, mysqlConfig.databaseName)
        mysqlDriver.createPeopleTableFromDataFrame(dataFrame)
        mysqlDriver.closeConnection()




