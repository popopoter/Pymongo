def stringChecker(stringToCheck):
    return isinstance(stringToCheck, basestring)

def floatChecker(floatToCheck):
    return isinstance(floatToCheck,float) or isinstance(floatToCheck,int)
def pointChecker(pointToCheck):
    return (pointToCheck['type']=='Point' and len(pointToCheck['coordinates']) == 2 and floatChecker(pointToCheck['coordinates'][0]) and floatChecker(pointToCheck['coordinates'][1]) )
def idChecker(idToCheck):
    return True