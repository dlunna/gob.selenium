from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# para base de datos
import mysql.connector

tiempo = 3

mydb = mysql.connector.connect(
    host="sisinv.upp.edu.mx",
    user="inventario2019",
    passwd="1a2s3d4f.",
    database="inventario2019",
)

# inicializando la base de gatos
mycursor = mydb.cursor()

# Haciendo una busqueda en la base de datos
mycursor.execute("SELECT * FROM inventario_impresionmodel")
myresult = mycursor.fetchall()

# Driver de Chrome
driver = webdriver.Chrome(executable_path='/var/www/pyfy/gob.selenium/chromedriver')
#Abrir página de login
driver.get('http://sirit.hidalgo.gob.mx/')
time.sleep(tiempo)

usuario = driver.find_element_by_id("email")
usuario.send_keys("mi_usuario_de_SIRIT")
usuario.send_keys(Keys.ENTER)
time.sleep(tiempo)

clave = driver.find_element_by_id("password")
clave.send_keys("mi_contraseña_de_SIRIT")
clave.send_keys(Keys.ENTER)
clave = driver.find_element_by_id("login")
clave.send_keys(Keys.ENTER)
time.sleep(tiempo)

for row in myresult:
    print(row)

    ## Abriendo otra ventana
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("http://sirit.hidalgo.gob.mx/Inicio/HARDWARE/IMPRESI%C3%93N")
    time.sleep(tiempo)

    ## Ingresando información
    clave = driver.find_element_by_id("no_Inventario")
    clave.send_keys(row[1])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("Tipo_Impresion")
    clave.send_keys(row[2])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("Impresion_Marca")
    clave.send_keys(row[3])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("Conexion_Impresion")
    clave.send_keys(row[4])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("modelo_Servidor")
    clave.send_keys(row[5])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    mensaje5 = row[6]
    mensaje5a = mensaje5.find("B/N")
    print("B/N :: ", mensaje5a)
    if mensaje5a >= 0:
        clave = driver.find_element_by_xpath("/html/body/div/div/div[3]/form/div[6]/div[6]/label/div/label[1]/input")
        clave.click()
    time.sleep(tiempo)

    mensaje5 = row[6]
    mensaje5a = mensaje5.find("COLOR")
    print("Color :: ", mensaje5a)
    if mensaje5a >= 0:
        clave = driver.find_element_by_xpath("/html/body/div/div/div[3]/form/div[6]/div[6]/label/div/label[2]/input")
        clave.click()
    time.sleep(tiempo)

    buscar_por_xpath=driver.find_element_by_xpath("/html/body/div/div/div[3]/form/button")
    time.sleep(tiempo)
    buscar_por_xpath.send_keys(Keys.ENTER)
    time.sleep(5)

    ## Cerrando la pestaña
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    #Fin del FOR

#Cerrando ventana del navegador
driver.switch_to.window(driver.window_handles[0])
driver.close()