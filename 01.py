from selenium import webdriver

driver = webdriver.Chrome(executable_path='/var/www/pyfy/gob.selenium/chromedriver')
driver.get('https://www.python.org')
driver.close()