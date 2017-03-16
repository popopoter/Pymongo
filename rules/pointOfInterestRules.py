import typeCheckers

validNames = {"name":typeCheckers.stringChecker,
            "kind":typeCheckers.stringChecker,
            "score":typeCheckers.floatChecker,
            "avg_price":typeCheckers.floatChecker,
            "city_id":typeCheckers.idChecker
            }