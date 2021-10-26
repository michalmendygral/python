import pymongo

class Database(object):
    URI = "mongodb://localhost:27017"#Universal resource identifir
    DATABASE = None

    @staticmethod # if we are not gonna using self
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)


    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection,query):
        return Database.DATABASE[collection].find_one(query)