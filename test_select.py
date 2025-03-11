from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select



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




    # Trouver le menu déroulant
    tri_element = wait.until(EC.visibility_of_element_located((By.ID, 'list-sort-select')))
    select_tri = Select(tri_element)

    assert select_tri.first_selected_option.text == "Meilleures ventes"

    select_tri.select_by_visible_text("Prix croissants")
    assert select_tri.first_selected_option.text == "Prix croissants"

    select_tri.select_by_index(3)
    assert select_tri.first_selected_option.text == "Remise décroissante"

    select_tri.select_by_value("4")
    assert select_tri.first_selected_option.text == "Note des clients"
