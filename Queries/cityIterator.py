from objects import city
class CityIterator(object):
    def __init__(self,cursor):
        self.cursor = cursor
        self.__next__ = None
    def prepareNext(self):
        nextItem= next(self.cursor,None)
        if(nextItem is not None):
            self.__next__ = city.city(**nextItem)
            return True
        return False
    def next(self):
        return self.__next__
