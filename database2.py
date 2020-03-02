import pymysql

# Conectar con base de datos
conexion = pymysql.connect(host="localhost",
                           port="3306",
                           user="inventario2019",
                           password="1a2s3d4f.",
                           database="inventario2019",
                           )

#cursor = conexion.cursor()

# Recuperar registros de la tabla 'Usuarios'
#registros = "SELECT * FROM inventario_energiamodel;"

# Mostrar registros
#cursor.execute(registros)
#filas = cursor.fetchall()
#for fila in filas:
#   print(fila)

# Finalizar
#conexion.commit()
conexion.close()