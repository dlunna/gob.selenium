import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="inventario2019",
    passwd="1a2s3d4f.",
    database="inventario2019",
)

#print(mydb)

mycursor = mydb.cursor()

## Para listar bases de datos
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

## Para crear una base de datos
#mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

## Para listar tablas
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

## Formula para insertar valores
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"

## Para insertar uno
student1 = ("Rachel", 22)
mycursor.execute(sqlFormula, student1)

## Para insertar multiples
students = [("Martha", 18),
            ("Iashchir", 18),
            ("Zulema", 13),
            ("Verenice", 28),]
mycursor.executemany(sqlFormula, students)

## Para seleccionar ALL
print("Select * -----------------")
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

mycursor.execute("SELECT * FROM students WHERE name='Zulema'")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)


mycursor.execute("SELECT * FROM inventario_almacenamientomodel")
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

