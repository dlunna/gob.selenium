import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="inventario2019",
    passwd="1a2s3d4f.",
    database="inventario2019",
)

#print(mydb)

mycursor = mydb.cursor()

## Para seleccionar ALL
print("Select * -----------------")
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

print("Select Nombre especifico -----------------")
mycursor.execute("SELECT * FROM students WHERE name='Zulema'")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

print("Select Inicio de texto -----------------")
mycursor.execute("SELECT * FROM students WHERE name LIKE 'Zu%'")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

print("Select Inicio y fin de texto -----------------")
mycursor.execute("SELECT * FROM students WHERE name LIKE '%ma%'")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

print("Select variable -----------------")
sql = "SELECT * FROM students WHERE name = %s"
mycursor.execute(sql, ("Martha",))
myresult = mycursor.fetchall()
for row in myresult:
    print(row)



## Para seleccionar uno
#mycursor.execute("SELECT age FROM students")
#oneresult = mycursor.fetchone()
#for row in oneresult:
#    print(row)


mydb.commit()
mydb.close()

