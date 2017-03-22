from objects import pointOfInterest
class POIIterator(object):
    def __init__(self,cursor):
        self.cursor = cursor
        self.__next__ = None
    def prepareNext(self):
        nextItem= next(self.cursor,None)
        if(nextItem is not None):
            self.__next__ = pointOfInterest.pointOfInterest(**nextItem)
            return True
        return False
    def next(self):
        return self.__next__
