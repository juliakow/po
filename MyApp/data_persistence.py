# klasa ktore umozliwia przechowywanie danych w pamieci
class DataPersistence:
    def __init__(self):
        self.data = {}

    # dodawanie nowych danych
    def store_data(self, timestamp, data):
        self.data[timestamp] = data

    # umozliwia pobranie danych dla danego timestampu
    def get_data(self, timestamp):
        return self.data.get(timestamp)