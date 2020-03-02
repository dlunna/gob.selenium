import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="inventario2019",
    passwd="1a2s3d4f.",
    database="inventario2019",
)

mycursor = mydb.cursor()

## Actualizar valores
sql = "UPDATE students SET age=22 WHERE name = 'Martha'"
mycursor.execute(sql)

## Para seleccionar ALL
print("Select * -----------------")
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)


## Para seleccionar por cantidad
print("Select by an specific number -----------------")
mycursor.execute("SELECT * FROM students LIMIT 5")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

## Con OFFSET
print("OFFSET oculta N numer ----------------------------")
mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 3")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)


mydb.commit()
mydb.close()

