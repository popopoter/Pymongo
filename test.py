from WikicityDB import connection
from objects import city
conexion= connection.Conection()

cliente = conexion.conected()
result = cliente.city.find()
resultado = city.CityIterator(result)
while(resultado.prepareNext()):
    print resultado.next().content

