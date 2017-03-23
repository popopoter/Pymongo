

def query1(comunidadAutonoma):
    consulta = [{'$match': {'autonomous_community':comunidadAutonoma}},{'$project' :{'name':1,'_id':0}}]
    return consulta
def query2(comunidadAutonoma):
    consulta = [{'$group':{
    '_id':comunidadAutonoma,
    'avgElevation':{'$avg':'$elevation'}}}]
    
    return consulta
def query3(comunidadAutonoma):
    consulta = [{'$group':{
    '_id':comunidadAutonoma,
    'avgDensity':{'$avg':{'$divide':['$population','$area']}}}}]
    
    return consulta
def query4(provincia):
    consulta = [
    {'$match':{'name':provincia}},
    {
        '$lookup':
            {
                'from':'POI',
                'localField':'_id',
                'foreignField':'city_id',
                'as': 'poi'
            }
    },
    {'$project':{'poi.kind':1,'_id':0}},
    {'$group':{'_id':'$poi.kind'}},
    {'$unwind':'$_id'},
    {'$group':{'_id':'$_id','count':{'$sum':1}}}
]
    
    return consulta
def query5(provincia):
    consulta = [
    {'$match':{'name':provincia}},
    {
        '$lookup':
            {
                'from':'POI',
                'localField':'_id',
                'foreignField':'city_id',
                'as': 'poi'
            }
    },
    {'$project':{'poi.kind':1,'_id':0}},
    {'$group':{'_id':'$poi.kind'}},
    {'$unwind':'$_id'},
    {'$group':{'_id':'$_id'}}
]
    
    return consulta
def query6(provincia,tipoPOI):
    consulta = [
{'$lookup':{'from':'POI','localField':'_id','foreignField':'city_id','as': 'poi'}},
{'$match':{'name':provincia}},
{'$unwind':'$poi'},
{'$match':{ 'poi.kind':tipoPOI}},
{'$group':{'_id':'$name','avgPrice':{'$avg':'$poi.avg_price'},'minPrice':{'$min':'$poi.avg_price'},'maxPrice':{'$max':'$poi.avg_price'}}},
]
    
    return consulta
def query7(tipoPOI,CoordenadaX, CoordenadaY):
    consulta = [
        {"$geoNear":
             {"near": { "type": "Point", "coordinates": [ CoordenadaX,CoordenadaY] }, "distanceField": "dist.calculated", "spherical": "true"}},
        {'$lookup':{'from':'POI','localField': '_id','foreignField':'city_id','as': 'cityPOI'}},
    {"$unwind":"$cityPOI"},{"$project":{"_id":0,"cityPOI.name":1,"name":1,"cityPOI.kind":1}},
    {'$match':{"cityPOI.kind":"Restaurant"}}]

    
    return consulta
def query8(tipoPOI,CoordenadaX, CoordenadaY,radio):
    consulta = [
    {'$lookup':{'from':"city",'localField': "city_id",'foreignField':"_id",'as': "cityPOI"}},
    {'$project':{"_id":0,"name":1,"kind":1,"cityPOI.name":1,"cityPOI.location":1}},
    {'$match':{"kind":tipoPOI}},
    {'$match':{"cityPOI.location":{"$geoWithin": {"$centerSphere": [[CoordenadaX,CoordenadaY],radio]}}}},
    {'$project': {"name":1,"kind":1,"citiPOI.location":1}},
    {'$limit': 5}]

    
    return consulta

def query9(tipoPOI):
    consulta = [
    {'$match':{'kind':tipoPOI}},
	{'$lookup':
            {
                'from':'city',
                'localField':'city_id',
                'foreignField':'_id',
                'as': 'city'
            }},
    {'$group': {'_id': '$name','cities':{'$addToSet':'$city.name'}}},
	{'$project' : {'_id':1,'cities':1,'size_of_cities':{'$size':'$cities'}}},
	{'$match': { 'size_of_cities' :{'$gt':1}}}
]
    return consulta
def query10():
    consulta = [
    {'$sort': {'score': -1}},
    {'$lookup': { 'from':'city',  'localField':'city_id','foreignField':'_id', 'as': 'city'}},
    {'$group': {'_id': '$city.name', 'POI': {'$push':{'name' :'$name', 'score':'$score'}}}},
    {'$project': {'city':'$_id','_id':0,"bestPOIs": { '$slice': [ "$POI", 3]}}},
    {'$out':'POIoftheyear'}
	 ]
    
    return consulta
def query11(tipoPOI):
    consulta = [
    {'$match':{'kind':tipoPOI}},
    {'$group': {'_id': '$name','count':{'$sum':1}}},
    {'$sort':{'count':1}},
    {'$limit': 5}
]
    return consulta

