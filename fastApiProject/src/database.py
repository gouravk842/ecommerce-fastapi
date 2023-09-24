from pymongo import MongoClient


# it creates instance of the database that is used throughout the application to interact with the database
class DatabaseManager:
    def __init__(self, db_name):
        self.client = MongoClient(uuidRepresentation='standard')
        self.db = self.client[db_name]

    def get_database(self):
        return self.db
