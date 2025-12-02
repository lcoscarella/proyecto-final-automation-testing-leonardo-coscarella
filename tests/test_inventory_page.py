from page.inventory_page import InventoryPage
from page.login_page import LoginPage
import utils.ancillary as utils
from utils import data_productos
from selenium.webdriver.common.by import By

from tests.conftest import logger

def test_InventarioSauceDemo(driver,tomarCaptura):
    
    inventoryPage = InventoryPage(driver)   
    inventoryPage.open()
    # Chequea que estoy en el inventario
    assert inventoryPage.prodInventoryCount > 0

    logger.info(f"Cantidad de productos en inventario: {inventoryPage.prodInventoryCount}")

    tomarCaptura("Inventario_1_presenciaDeProductosEnInventario")

    # Abro Menu con un click y chequeo que haya al menos una opcion
    inventoryPage.openMenu()

    assert len(driver.find_elements(By.CLASS_NAME, 'bm-item')) > 0

    tomarCaptura("Inventario_2_menuAbiertoConOpciones")

    logger.info("Menú abierto con opciones visibles.")

    # Cierro Menu con un click y chequeo que el menu se haya cerrado
    inventoryPage.closeMenu()

    tomarCaptura("Inventario_3_menuCerrado")

    logger.info("Menú cerrado correctamente.")

    # Ordeno listado de productos por nombre (Z a A) y luego por precio (menor a mayor)
    inventoryPage.sortItems("za")
    tomarCaptura("Inventario_4_productosOrdenadosPorNombre")

    logger.info("Productos ordenados por nombre (Z a A).")

    inventoryPage.sortItems("lohi")
    tomarCaptura("Inventario_5_productosOrdenadosPorPrecio")
    logger.info("Productos ordenados por precio (menor a mayor).")

    # Agrego productos al carrito y chequeo que el badge del carrito se actualice
    lista_productos = data_productos.leer_datos_productos('data/productos.json')

    for producto in lista_productos:
        inventoryPage.addItemToCartByName(producto)
        tomarCaptura(f"Inventario_productoAgregadoAlCarrito_{producto}")

    assert inventoryPage.getCartBadgeCount() == lista_productos.__len__()
    logger.info(f"Productos agregados al carrito: {lista_productos.__len__()}")

    # Abro el carrito y chequeo que los productos estén presentes
    inventoryPage.openCart()
    assert inventoryPage.getNumberOfProducts() > 0

    tomarCaptura("Inventario_8_carritoConProductosAgregados")
    logger.info("Carrito abierto con productos agregados presentes.")

    # Elimino los productos del carrito y chequeo que el badge del carrito desaparezca
    for _ in range(inventoryPage.getNumberOfProducts()):
        inventoryPage.removeItemFromCart()
    
    assert inventoryPage.getCartBadgeCount() == 0

    tomarCaptura("Inventario_9_carritoVacioDespuesDeEliminarProductos")
    logger.info("Productos eliminados del carrito correctamente. Carrito vacío.")


