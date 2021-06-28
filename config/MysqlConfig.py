from Database.Driver import Driver


class MysqlConfig(Driver):
    def __init__(self):
        super().__init__("root", "03091977s", "localhost", "3306", "test")