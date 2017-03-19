from rules import cityRules
from pointOfInterest import pointOfInterest
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
            poiContent = [x.save() for x in self.POI]
            return [self.content,poiContent]
        return {k:v for k,v in self.content.iteritems() if(k in self.changed)}