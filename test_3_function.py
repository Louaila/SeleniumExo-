from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pytest
from selenium import webdriver



@pytest.fixture
# Toutes les choses que tu veux faire plein de fois comme l'overture de la page ou la ferture 
#  La fixture Navigate gère maintenant l'initialisation et la fermeture du navigateur , ça evite les repetitions du code 
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    #  Instancier le navigateur Chrome avec les options
    browser = webdriver.Chrome(options)

    # Ouvrir en plein écran
    browser.maximize_window()

    yield browser
    
     # Fermer le navigateur
    browser.quit()



@pytest.fixture
def wait(driver):
    # Instantiating explicit wait for the given driver
    return WebDriverWait(driver, 10)








def test_search_product(driver,wait):

    # Naviguer vers le site de décathlon
    driver.get("https://www.decathlon.fr/")

    # Vérifier que le titre de la page est correct
    assert driver.title == 'DECATHLON | Magasin de Sport'

    # Continuer sans accepter les cookies
    try:
        wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "didomi-continue-without-agreeing"))
            ).click()
    except NoSuchElementException:
        print("Cookies pop-up is not present")

    # Récupérer le champ de recherche en utilisant le xpath
    search_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='search']"))
        )

    # Ecrire Vélo dans le champ de recherche et simuler le bouton Entrée
    search_box.clear()
    search_box.send_keys("Vélo")
    search_box.send_keys(Keys.RETURN)

    # Vérifier que nous sommes sur la page des vélos
    resultatRecherche = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        ).text
    assert resultatRecherche == "Vélos"

    #  Vérifier qu'il y a au moins un produit affiché
    product_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product-list')))
    assert product_list.is_displayed(), "Products should be visible"

   
 

