from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from page.login_page import LoginPage

import utils.ancillary as utils

class InventoryPage:

    badge = "0"
    prodInventoryCount = 0

    # Constructor
    def __init__(self,driver):
        self.driver = driver

    # Método para abrir la página de inventario
    def open(self):

        Login = LoginPage(self.driver)
        Login.open()
        Login.login(username=utils.sauceDemoUser,password=utils.sauceDemoPwd)

        #self.driver.get(utils.sauceDemoInventoryUrl)    
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("/inventory.html")
        )

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        self.prodInventoryCount = len(self.driver.find_elements(By.CLASS_NAME, 'inventory_item'))
        

    def openMenu(self):
        botonMenu = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        botonMenu.click()

    def closeMenu(self):
        botonCerrarMenu = self.driver.find_element(By.ID, 'react-burger-cross-btn')
        botonCerrarMenu.click()

    def sortItems(self,criteria):
        selectElement = self.driver.find_element(By.CLASS_NAME, 'product_sort_container')
        select = Select(selectElement)
        select.select_by_value(criteria)

    def addItemToCartByName(self,productName):
        items = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')
        for item in items:
            name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text.strip()
            if name == productName:
                botonAgregar = item.find_element(By.TAG_NAME, 'button')
                botonAgregar.click()
                self.badge = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text.strip()
                break
    
    def getCartBadgeCount(self):
        return int(self.badge)

    def openCart(self):
        carrito = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        carrito.click()

    def getNumberOfProducts(self):
        products = self.driver.find_elements(By.CLASS_NAME, 'cart_item_label')
        return len(products)

    def removeItemFromCart(self):
        items = self.driver.find_elements(By.CLASS_NAME, 'cart_button')
        if len(items) > 0:
            items[0].click()
            self.badge = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text.strip() if len(self.driver.find_elements(By.CLASS_NAME, 'shopping_cart_badge')) > 0 else "0"
