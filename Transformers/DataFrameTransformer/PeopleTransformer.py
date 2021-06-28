import pandas as pd
class PeopleTransformer:
    def __init__(self, data):
        self.data = data
    def transform(self):
        df = pd.DataFrame(self.data, columns=["name", 'height', "gender", "homeWorld", "starShip.name"])
        return df