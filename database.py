#import mysql.connector as mariadb
import mariasql
# decodigo.com
#mariadb_conexion = mariadb.connect(host='localhost', port='3306',
#                                   user='root', password='password', database='Pruebas')

mariadb_conexion = mariasql.MariaSQL.connect(host='localhost', port='3306', user='inventario2019',
                                             password='1a2s3d4f.', database='inventario2019')

cursor = mariadb_conexion.cursor()

try:
    cursor.execute("SELECT ID,TIPO,MARCA,INVENTARIO FROM inventario_energiamodel")
    for id, tipo, marca, inventario in inventario_energiamodel:
        print("id: " + str(id))
        print("tipo: " + tipo)
        print("marca: " + marca)
        print("inventario: " + inventario)
except mariadb.Error as error:
    print("Error: {}".format(error))
mariadb_conexion.close()