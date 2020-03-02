from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# para base de datos
import mysql.connector

tiempo = 0.4

mydb = mysql.connector.connect(
    host="sisinv.upp.edu.mx",
    user="inventario2019",
    passwd="1a2s3d4f.",
    database="inventario2019",
)

# inicializando la base de gatos
mycursor = mydb.cursor()

# Haciendo una busqueda en la base de datos
mycursor.execute("SELECT * FROM inventario_felixmodel")
mycpu = mycursor.fetchall()

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

for row in mycpu:
    print(row)

    ## Abriendo otra ventana
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("http://sirit.hidalgo.gob.mx/Inicio/HARDWARE/EQUIPO%20DE%20COMPUTO%20PERSONAL")
    time.sleep(tiempo)

    ## Ingresando información
    clave = driver.find_element_by_id("personal_inventario")
    clave.send_keys(row[1])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("personal_tipo")
    clave.send_keys(row[2])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("personal_marca")
    clave.send_keys(row[3])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("personal_modelo")
    clave.send_keys(row[4])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("personal_procesador")
    clave.send_keys(row[5])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("Velocidad_Procesador")
    clave.send_keys(row[6])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("personal_Ram")
    clave.send_keys(row[7])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("personal_SO")
    clave.send_keys(row[8])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("Version_SO")
    clave.send_keys(row[9])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("personal_Almacenamiento")
    clave.send_keys(row[10])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("puertos_USB")
    clave.send_keys(row[11])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("personal_arquitectura")
    clave.send_keys(row[12])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("personal_licencia")
    clave.send_keys("Si")
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    mensaje5 = row[14]
    mensaje5a = mensaje5.find("Alambrica")
    print("Alambrica :: ", mensaje5a)
    if mensaje5a >= 0:
        clave = driver.find_element_by_id("personal_conexion0")
        clave.click()
    time.sleep(tiempo)

    #mensaje5 = row[14]
    mensaje5a = mensaje5.find("Inalambrica")
    print("Inalambrica :: ", mensaje5a)
    if mensaje5a >= 0:
        clave = driver.find_element_by_id("personal_conexion1")
        clave.click()
    time.sleep(tiempo)


    ##Fin de CPU
    # -------------------------------------------------------------

    ## Inicio Monitor

    clave = driver.find_element_by_id("AddMonitor")
    #clave.send_keys(row[15])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("monitor_inventario")
    clave.send_keys(row[15])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("marca_monitor")
    clave.send_keys(row[16])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("modelo")
    clave.send_keys(row[17])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("tamanio")
    clave.send_keys(row[18])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("tipo_pantalla")
    clave.send_keys(row[19])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    clave = driver.find_element_by_id("resolucion")
    clave.send_keys(row[20])
    clave.send_keys(Keys.ENTER)
    time.sleep(tiempo)

    mensaje5 = row[21]
    mensaje5a = mensaje5.find("Display Port")
    print("B/N :: ", mensaje5a)
    if mensaje5a >= 0:
        clave = driver.find_element_by_xpath("/html/body/div/div/div[3]/form/div[6]/div/div[16]/div/div[7]/label/div/label[1]/input")
        clave.click()
    time.sleep(tiempo)

    mensaje5 = row[21]
    mensaje5a = mensaje5.find("VGA")
    print("Color :: ", mensaje5a)
    if mensaje5a >= 0:
        clave = driver.find_element_by_xpath("/html/body/div/div/div[3]/form/div[6]/div/div[16]/div/div[7]/label/div/label[2]/input")
        clave.click()
    time.sleep(tiempo)

    mensaje5 = row[21]
    mensaje5a = mensaje5.find("HDMI")
    print("Color :: ", mensaje5a)
    if mensaje5a >= 0:
        clave = driver.find_element_by_xpath("/html/body/div/div/div[3]/form/div[6]/div/div[16]/div/div[7]/label/div/label[3]/input")
        clave.click()
    time.sleep(tiempo)

    ## Fin de Monitor

    #-------------------------GUARDANDO-----------------#
    buscar_por_xpath = driver.find_element_by_xpath("/html/body/div/div/div[3]/form/button")
    #time.sleep(tiempo)
    buscar_por_xpath.send_keys(Keys.ENTER)
    time.sleep(5)
    # -------------------------GUARDANDO-----------------#

    ## Cerrando la pestaña
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
#Fin del FOR

#Cerrando ventana del navegador
driver.switch_to.window(driver.window_handles[0])
driver.close()