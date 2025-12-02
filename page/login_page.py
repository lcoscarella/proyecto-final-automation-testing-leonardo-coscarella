from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import utils.ancillary as utils

class LoginPage:
    # La variable error_message almacenará el mensaje de error en caso de que el login falle
    error_message = ""

    # Constructor
    def __init__(self,driver):
        self.driver = driver

    # Método para abrir la página de login
    def open(self):
        self.driver.get(utils.sauceDemoUrl)

    # Método para realizar el login
    def login(self,username=utils.sauceDemoUser,password=utils.sauceDemoPwd):
        # Ingresar usuario, pwd y enviar click en boton Submit
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.NAME,utils.sauceDemoInputUsername))
        ).send_keys(username)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.NAME,utils.sauceDemoInputPassword))
        ).send_keys(password)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.NAME,utils.sauceDemoInputLoginButton))
        ).click()

        # Capturo el mensaje de error en caso de que el login falle
        try:
            self.error_message = str(self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text)
        except:
            self.error_message = ""