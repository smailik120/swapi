from sqlalchemy import create_engine

from Database.Driver import Driver


class MysqlDriver(Driver):
    def __init__(self, login, password, hostName, port, databaseName):
        super().__init__(login, password, hostName, port, databaseName)
        self.name = "mysql"
        self.connection()
    def connection(self):
        engine = create_engine(f"{self.name}://{self.login}:{self.password}@{self.hostName}:{self.port}/{self.databaseName}", echo=True)
        self.mysqlConnection = engine.connect()

    def createPeopleTableFromDataFrame(self, df):
        sqlite_table = "people"
        df.to_sql(sqlite_table, self.mysqlConnection, if_exists='replace', index=False)

    def closeConnection(self):
        self.mysqlConnection.close()
