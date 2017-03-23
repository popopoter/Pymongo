from Conexion import connection
from rules import pointOfInterestRules
from Queries import consultas
conexion= connection.Conection()
cliente = conexion.conected()
class pointOfInterest(object):
    myRules = pointOfInterestRules.validNames

    def __init__(self, **args):
        self.id = args['id'] if 'id' in args.keys() else None
        # Borramos los poi del dicionario si no tienen no lanza excepcion
        self.content = {k: v for k, v in args.iteritems() if (k in self.myRules.keys() and self.myRules.get(k)(v))}
        self.changed = []

    def update(self, name, value):
        if (name in self.myRules and self.myRules.get(name)(value)):
            self.changed.append(name)
            self.content.update({name: value})
        else:
            print "Error [" + name + ':' + value + "]"

    def save(self):
        if self.id is None:
            #poiContent = [x.save() for x in self.POI]
            cliente.POI.insert(self.content)

        else:
            if len(self.changed)>0:
                pairs = {k: v for k, v in self.content.iteritems() if (k in self.changed)}
                cliente.POI.update({'_id': self.id}, {'$set': pairs})
                self.changed = []
    @staticmethod
    def query(string):
        consulta= cliente.POI.aggregate(string)
        return POIIterator(consulta)

class POIIterator(object):
    def __init__(self,cursor):
        self.cursor = cursor
        self.__next__ = None
    def prepareNext(self):
        nextItem= next(self.cursor,None)
        if(nextItem is not None):
            self.__next__ = pointOfInterest(**nextItem)
            return True
        return False
    def next(self):
        return self.__next__

consulta=cliente.POI.find_one()
poi = pointOfInterest(**consulta)
#ciudad.update('name', 'Sevilla')
poi.save()
query=poi.query(consultas.query8('Cafe',40,-5,100))
while(query.prepareNext()):
   print query.next().content

