import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="inventario2019",
    passwd="1a2s3d4f.",
    database="inventario2019",
)

mycursor = mydb.cursor()

## Ordenados de manera ascendente
print("Ordenados de manera ascendente")
sql = "SELECT * FROM students ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for r in myresult:
    print(r)

## Ordenados de manera descendente
print("Ordenados de manera descendente")
sql = "SELECT * FROM students ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for r in myresult:
    print(r)


## Para seleccionar ALL
print("Select * -----------------")
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
#for row in myresult:
#    print("alo", row)


#mydb.commit()
mydb.close()

