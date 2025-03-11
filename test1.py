from selenium import webdriver
from selenium.webdriver.common.by import By

 
"""
Définir des options pour le driver. Pour chrome, garder
le navigateur ouvert si driver.quit() n'est pas appelée
"""
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
#  Instancier le navigateur Chrome avec les options
driver = webdriver.Chrome(options)
 
# Ouvrir en plein écran
driver.maximize_window()
 
# Naviguer vers le site de décathlon
driver.get("https://www.decathlon.fr/")
 
# Vérifier que le titre de la page est correct
assert driver.title == 'DECATHLON | Magasin de Sport'
 
# Vérifier que le titre de la page est correct
assert driver.current_url == 'https://www.decathlon.fr/'
 
# Fermer le navigateur
driver.quit()


 

# driver.find_elemen(by.ID, "button1").click()

# Localisation par id :       element = driver.find_element(By.ID, "user")
# Localisation par classe :       element = driver.find_element(By.CLASS_NAME, "content")
# Localisation par nom :      element = driver.find_element(By.NAME, "login")
# Localisation par balise :       element = driver.find_element(By.TAG_NAME, "h1")
# Localisation par texte :        element = driver.find_element(By.LINK_TEXT, "Retour page accueil")
# Localisation par texte partiel :    element = driver.find_element(By.PARTIAL_LINK_TEXT, "page accueil")
# Localisation par xpath :    element = driver.find_element(By.XPATH, "//p[text()='Texte pour XPATH']")
# Localisation par CSS :  element = driver.find_element(By.CSS_SELECTOR, ".btn-css-selector")