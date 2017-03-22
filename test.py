from Conexion import connection
from Queries import cityIterator
from objects import city
conexion= connection.Conection()

cliente = conexion.conected()
result = cliente.city.find()
resultado = cityIterator.CityIterator(result)
while(resultado.prepareNext()):
    print resultado.next().content

