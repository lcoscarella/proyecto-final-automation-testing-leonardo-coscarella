from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

sauceDemoUrl = 'https://www.saucedemo.com/'
sauceDemoUser = 'standard_user'
sauceDemosInvalidUser = "usuario_invalido"
sauceDemoPwd = 'secret_sauce'
sauceDemoInvalidPwd = "pwd_invalida"
sauceDemoInventoryUrl = 'https://www.saucedemo.com/inventory.html'
sauceDemoCartUrl = 'https://www.saucedemo.com/cart.html'

sauceDemoInputUsername = 'user-name'
sauceDemoInputPassword = 'password'
sauceDemoInputLoginButton = 'login-button'

def getDriver():

    # Inicialización de driver

    # Las siguientes options se utilizan para que no aparezcan ventanas emergentes (cambio de contraseña en Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=PasswordCheck")
    options.add_argument("--disable-features=AutofillServerCommunication")

    options.add_argument("--incognito")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")


    options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    })


    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=options)

    time.sleep(1)

    return driver