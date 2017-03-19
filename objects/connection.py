from pymongo import MongoClient
class Conection(object):
    client = None
    @staticmethod
    def conected():
        Conection.client= MongoClient()
        return Conection.client.WikiCity