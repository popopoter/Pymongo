import json

from objects.city import city

with open('wikicity.json','r') as f:
    for line in f:
        jsons = json.loads(line)
    f.close()

#ciudades = [city(**x) for x in jsons]
#for x in jsons:
    #print type(ciudades[0].content['location']['coordinates'])
    #print(x)

client = MongoClient('mongodb://localhost:27017/')

'''dbCity = client['wikicity'].city
dbPOI = client['wikicity'].POI
nuevoId = dbCity.insert([x.content for x in ciudades])
print nuevoId
for i in range(0,len(nuevoId)):
    ciudades[i].id = nuevoId[i]
    for poi in ciudades[i].POI:
        poi.update('city_id',nuevoId[i])
        dbPOI.insert(poi.save())
'''
#ciudades[0].update('name','asd')
#print ciudades[0].content['name']
#texto = ciudades[0].save()

dbCity = client['wikicity'].city
dbPoi = client['wikicity'].POI
'''
for ci in cities:
    ci.POI = dbPoi.find({'city_id': ci.id})
for ci in cities:
    print ci.content
    for cosa in ci.POI:
        print cosa
        #text = texto[0].__str__()[:-1]+", u'POI':" + texto[1].__str__() + "}"
queryCity = dbCity.find()

'''
#Ciudades por comundad
responso = dbCity.aggregate([{'$match': {'autonomous_community':'Castilla y Leon'}},{'$project' :{'name':1,'_id':0}}])
#Altura de ciudades por comundad
responso = dbCity.aggregate([{'$group':{
    '_id':'$autonomous_community',
    'avgElevation':{'$avg':'$elevation'}}}])
#densidad  media de las ciudades de una comunidad autonoma
responso = dbCity.aggregate([{'$group':{
    '_id':'$autonomous_community',
    'avgDensity':{'$avg':{'$divide':['$population','$area']}}}}])

responso = dbCity.aggregate([
    {
        '$lookup':
            {
                'from':'POI',
                'localField':'_id',
                'foreignField':'city_id',
                'as': 'poi'
            }
    }

])
responso = dbCity.aggregate([
    {'$match':{'name':'Salamanca'}},
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


])

responso = dbCity.aggregate([
    {'$match':{'name':'Salamanca'}},
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


])

responso = dbCity.aggregate([
    {'$match':{'name':'Salamanca'}},
    {
        '$lookup':
            {
                'from':'POI',
                'localField':'_id',
                'foreignField':'city_id',
                'as': 'poi'
            }
    },
    {'$project':{'poi.avg_price':1,'_id':0}},
    {'$unwind':'$poi'}
    #{'$group':{'_id':'null','avgPrice':{'$avg':'avg_price'}}}


])
#Ultima\
responso = dbPoi.aggregate([
    {'$match':{'kind':'Restaurant'}},
    {'$group': {'_id': '$name','count':{'$sum':1}}},
    {'$sort':{'count':1}},
    {'$limit': 5}

    #{'$group':{'_id':'null','avgPrice':{'$avg':'avg_price'}}}


])
for coso in responso:
    print coso

#cities =[city(**doc) for doc in queryCity]


#with open('wikiOut.json','w') as file:
    #json.dump(text,file)