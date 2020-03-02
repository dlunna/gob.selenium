from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/var/www/pyfy/gob.selenium/chromedriver')
driver.get('https://gmail.com')

usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("dl@site.upp.edu.mx")
usuario.send_keys(Keys.ENTER)
time.sleep(5)

clave = driver.find_element_by_name("password")
clave.send_keys("micontrasena")
clave.send_keys(Keys.ENTER)

time.sleep(50)

driver.close()