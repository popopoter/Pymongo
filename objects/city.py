from Conexion import connection
from rules import cityRules

from Queries import consultas

conexion= connection.Conection()
cliente = conexion.conected()
class city(object):
    myRules = cityRules.validNames
    def __init__(self,**args):
        self.id = args['_id'] if '_id' in args.keys() else None
        #self.id = args['city_id'] if 'city_id' in args.keys() else None
        self.content = {k:v for k,v in args.iteritems() if(k in self.myRules.keys() and self.myRules.get(k)(v))}
        self.changed = []
    def update(self,name,value):
        if(name in self.myRules and self.myRules.get(name)(value)):
            self.changed.append(name)
            self.content.update({name:value})
        else:
            print "Error ["+name+':'+value+"]"
    def save(self):
        if self.id is None:
            #poiContent = [x.save() for x in self.POI]
            cliente.city.insert(self.content)

        else:
            if len(self.changed)>0:
                pairs = {k: v for k, v in self.content.iteritems() if (k in self.changed)}
                cliente.city.update({'_id': self.id}, {'$set': pairs})
                self.changed = []
    @staticmethod
    def query(string):
        consulta= cliente.city.aggregate(string)
        return CityIterator(consulta)

class CityIterator(object):
    def __init__(self,cursor):
        self.cursor = cursor
        self.__next__ = None
    def prepareNext(self):
        nextItem= next(self.cursor,None)
        if(nextItem is not None):
            self.__next__ = city(**nextItem)
            return True
        return False
    def next(self):
        return self.__next__

if __name__ == "__main__":
    #dict = {'_id': 'ObjectID("67654646465sa65a76235373t")', 'name': 'Barcelona'}
    #ciudad= city(**dict)
    #ciudad.save()
    consulta=cliente.city.find_one()
    ciudad = city(**consulta)
    #ciudad.update('name', 'Sevilla')
    ciudad.save()
    query1=ciudad.query(consultas.query1('Castilla y Leon'))
    while(query1.prepareNext()):
        print query1.next().content