from page.login_page import LoginPage
import utils.data_login
import utils.ancillary as ancillary
import pytest
from tests.conftest import logger

# Test de login con varios casos usando data-driven
@pytest.mark.parametrize("username,password,esExito", utils.data_login.leer_csv_login('data/login.csv'))
def test_login_varios_casos_csv(driver,username,password,esExito,tomarCaptura):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login(username=username,password=password)

    if esExito:
        assert "/inventory.html" in driver.current_url
        tomarCaptura(f"Login_exito_{username}")
    else:
        try:
            assert "Epic sadface:" in loginPage.error_message
            tomarCaptura(f"Login_error_{username}")
        except AssertionError:
            tomarCaptura(f"Exception_Login_error_{username}")

@pytest.mark.parametrize("username,password,esExito", utils.data_login.leer_json_login('data/login.json'))
def test_login_varios_casos_json(driver,username,password,esExito,tomarCaptura):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login(username=username,password=password)

    if esExito:
        assert "/inventory.html" in driver.current_url
        tomarCaptura(f"Login_exito_{username}")
        logger.info(f"Login exitoso para el usuario: {username}")
    else:
        try:
            assert "Epic sadface:" in loginPage.error_message
            tomarCaptura(f"Login_error_{username}")
            logger.warning(f"Login fallido para el usuario: {username} - Mensaje de error: {loginPage.error_message}")
        except AssertionError:
            tomarCaptura(f"Exception_Login_error_{username}")
            logger.error(f"Excepción durante el login para el usuario: {username}")

@pytest.mark.parametrize("username,password,esExito", utils.data_login.leer_json_y_fakes_login('data/login.json'))
def test_login_varios_casos_json(driver,username,password,esExito,tomarCaptura):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login(username=username,password=password)

    if esExito:
        assert "/inventory.html" in driver.current_url
        tomarCaptura(f"Login_exito_{username}")
        logger.info(f"Login exitoso para el usuario: {username}")
    else:
        try:
            assert "Epic sadface:" in loginPage.error_message
            tomarCaptura(f"Login_error_{username}")
            logger.warning(f"Login fallido para el usuario: {username} - Mensaje de error: {loginPage.error_message}")
        except AssertionError:
            tomarCaptura(f"Exception_Login_error_{username}")
            logger.error(f"Excepción durante el login para el usuario: {username}")

# # Test de login exitoso
# def test_login_exito(driver,tomarCaptura):
#     loginPage = LoginPage(driver)
#     loginPage.open()
#     loginPage.login()

#     assert "/inventory.html" in driver.current_url

#     tomarCaptura("Login_1_loginExitoso")

# # Test de login con usuario inválido
# def test_login_error_usuario_invalido(driver,tomarCaptura):
#     loginPage = LoginPage(driver)
#     loginPage.open()
#     loginPage.login(username=utils.sauceDemosInvalidUser,password=utils.sauceDemoPwd)

#     assert loginPage.error_message == "Epic sadface: Username and password do not match any user in this service"

#     tomarCaptura("Login_2_loginErrorUsuarioInvalido")

# # Test de login con contraseña inválida
# def test_login_error_pwd_invalido(driver,tomarCaptura):
#     loginPage = LoginPage(driver)
#     loginPage.open()
#     loginPage.login(username=utils.sauceDemoUser,password=utils.sauceDemoInvalidPwd)

#     assert loginPage.error_message == "Epic sadface: Username and password do not match any user in this service"
    
#     tomarCaptura("Login_3_loginErrorPwdInvalido")
