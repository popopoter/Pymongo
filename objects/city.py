from WikicityDB import connection,consultas
from rules import cityRules

class City(object):
    myConnection = connection.Conection()
    myRules = cityRules.validNames
    def __init__(self,**args):
        self.id = args['_id'] if '_id' in args.keys() else None
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
            self.myConnection.conected().city.insert(self.content)
        else:
            if self.changed:
                pairs = {k: v for k, v in self.content.iteritems() if (k in self.changed)}
                self.myConnection.conected().city.update({'_id': self.id}, {'$set': pairs})
                self.changed = []
    @classmethod
    def query(*string):

        return CityIterator((City.myConnection.conected().city.aggregate(string[1])))

class CityIterator(object):
    def __init__(self,cursor):
        self.cursor = cursor
        self.__next__ = None
    def prepareNext(self):
        nextItem= next(self.cursor,None)
        if(nextItem is not None):
            self.__next__ = City(**nextItem)
            return True
        return False
    def next(self):
        return self.__next__

if __name__ == "__main__":

    query1 = City.query(consultas.query1('Castilla y Leon'))
    while(query1.prepareNext()):
        print query1.next().content
