from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

sauceDemoUrl = 'https://www.saucedemo.com/'
sauceDemoUser = 'standard_user'
sauceDemoPwd = 'secret_sauce'
sauceDemoCartUrl = 'https://www.saucedemo.com/cart.html'

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

    time.sleep(5)

    return driver

def loginSaucedemo(driver):

    # Abro la pagina de login
    driver.get(sauceDemoUrl)
    
    # Ingresar usuario, pwd y enviar click en boton Submit
    driver.find_element(By.NAME,'user-name').send_keys(sauceDemoUser)
    driver.find_element(By.NAME,'password').send_keys(sauceDemoPwd)
    driver.find_element(By.ID,'login-button').click()

    time.sleep(5)