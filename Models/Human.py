class Human:
    def __init__(self, name, homeWorld, height, gender, starShips):
        self.name = name
        self.homeWorld = homeWorld
        self.height = height
        self.gender = gender
        self.starShips = starShips

    def getHumanRecords(self):
        records = []
        if self.homeWorld == "Tatooine":
            starShips = self.starShips
            if len(starShips) > 0:
                for starShip in starShips:
                    record = [self.name, self.height, self.gender, self.homeWorld, starShip.name]
                    records.append(record)
            else:
                record = [self.name, self.height, self.gender, self.homeWorld, "-"]
                records.append(record)
        return records