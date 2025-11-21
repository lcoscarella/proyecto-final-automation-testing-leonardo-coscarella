import pytest
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.ancillary import getDriver,loginSaucedemo,sauceDemoCartUrl

@pytest.fixture
def driver():
    # Instanciar driver
    driver =  getDriver()
    yield driver
    driver.quit()

@pytest.fixture
def tomarCaptura(driver):
    ### Funcion para tomar captura de pantallas
    def tomar(nombre):
        timeStamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        path = f"capturas/{nombre}_{timeStamp}.png"
        driver.save_screenshot(path)
    return tomar

def test_loginSauceDemo(driver,tomarCaptura):

    loginSaucedemo(driver)

    # Chequea haber sido redirigido a la url de inventario
    assert "/inventory.html" in driver.current_url

    tomarCaptura("Login_1_loginExitoso")

    # Chequea elementos del inventario
    titulo  = driver.find_element(By.CLASS_NAME,"title").text.strip()
    assert titulo == 'Products'

    encabezado = driver.find_element(By.CLASS_NAME,"app_logo").text.strip()
    assert encabezado == "Swag Labs"

    tomarCaptura("Login_2_elementosInventarioPostLogin")

def test_InventarioSauceDemo(driver,tomarCaptura):
    
    # Login
    loginSaucedemo(driver)

    # Chequea nombre del titulo
    assert driver.find_element(By.CLASS_NAME,"title").text.strip() == 'Products'

    # Chequea la presencia de productos en el inventario
    assert len(driver.find_elements(By.CLASS_NAME, 'inventory_item')) > 0

    tomarCaptura("Inventario_1_presenciaDeProductosEnInventario")

    # Abro Menu con un click y chequeo que haya al menos una opcion
    botonMenu = driver.find_element(By.ID, 'react-burger-menu-btn')
    botonMenu.click()

    time.sleep(2)

    assert len(driver.find_elements(By.CLASS_NAME, 'bm-item')) > 0

    # Captura
    tomarCaptura("Inventario_2_menuAbierto")

    # Cerrar menu
    botonCerrarMenu = driver.find_element(By.ID, 'react-burger-cross-btn')
    botonCerrarMenu.click()

    time.sleep(2)

    # Ordeno listado de productos por nombre (Z a A) y luego por precio (menor a mayor)
    ddlSort = Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
    ddlSort.select_by_value("za")

    tomarCaptura("Inventario_3_productosOrdenadosPorNombre")

    time.sleep(4)

    ddlSort = Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
    ddlSort.select_by_value("lohi")

    tomarCaptura("Inventario_4_productosOrdenadosPorPrecio")

    time.sleep(4)

def test_CarritoSauceDemo(driver,tomarCaptura):
    # Login
    loginSaucedemo(driver)

    # Chequea la presencia de productos en el inventario
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    
    assert len(products) > 0

    # Agrego el primer producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    time.sleep(2)

    # Chequeo que el carrito se haya incrementado
    badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'shopping_cart_badge')))

    assert int(badge.text) > 0 

    tomarCaptura("Carrito_1_agregadoDeProducto_CarritoIncrementado")

    # Agrego el segundo producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[1].click()

    time.sleep(2)

    # Chequeo que el carrito se haya incrementado
    badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'shopping_cart_badge')))

    assert int(badge.text) > 0 

    tomarCaptura("Carrito_2_agregadoDeProducto_CarritoIncrementadoX2")

    # Abro el carrito
    driver.get(sauceDemoCartUrl)

    time.sleep(2)

    # Chequeo que haya al menos un producto en el carrito
    cartItems = driver.find_elements(By.CLASS_NAME, "cart_item_label")
    assert len(cartItems) > 0

    tomarCaptura("Carrito_3_detalleProductosCarrito")


### python -m pytest -v   
