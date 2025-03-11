from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
#  Instancier le navigateur Chrome avec les options
driver = webdriver.Chrome(options)

# Wait implicite
driver.implicitly_wait(5)
 

# Ouvrir en plein écran
driver.maximize_window()
 
# Naviguer vers le site de décathlon
driver.get("https://www.decathlon.fr/")




 
driver.find_element(By.ID, "didomi-notice-agree-button").click()

element = driver.find_element(By.XPATH, "//input[@placeholder='Rechercher un produit, un sport ou une référence']")
element.send_keys("ballon")
element.send_keys(Keys.RETURN)


