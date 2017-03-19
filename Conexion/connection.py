from rules import cityRules
import pymongo
import json
from pymongo import MongoClient
class Conection(object):
    client = None
    @staticmethod
    def conected():
        Conection.client= MongoClient()
        return Conection.client.Wikiciudad
lista = []
conexion= Conection()
cliente = conexion.conected()
ciudad= cliente.city
poi=cliente.POI
ciudad.create_index(u"name",unique=True)
ciudad.ensure_index([(u"location", pymongo.GEOSPHERE)])