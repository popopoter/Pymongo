from rules import pointOfInterestRules

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
            return self.content
        return {k: v for k, v in self.content.iteritems() if (k in self.changed)}