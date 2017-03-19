from pymongo import  MongoClient


client = None;

def getClient():
    if(client is not None):
        client  = MongoClient('mongodb://localhost:27017/')

    return client

