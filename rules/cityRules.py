import typeCheckers

validNames = {"name":typeCheckers.stringChecker,
              "province":typeCheckers.stringChecker,
              "autonomous_community": typeCheckers.stringChecker,
              "area":typeCheckers.floatChecker,
              "elevation":typeCheckers.floatChecker,
              "population":typeCheckers.floatChecker,
              "location":typeCheckers.pointChecker,
              "POI":typeCheckers.stringChecker,
              }