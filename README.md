### #########################################################
### Propósito del proyecto
### Esta es la entregacfinal del curso de Automation Testing de Talento Tech
### Nombre y Apellido: Leonardo Coscarella

### Tecnologías utilizadas
### Python, Selenium Web Driver, Pytest JavaScript, CSS, DOM, HTML, POM, API HTTP requests, Logger

### Instrucciones de instalación de dependencias
### Se debe importar las siguientes dependencias:
### from utils.ancillary import getDriver,loginSaucedemo,sauceDemoCartUrl

### Comando para ejecutar las pruebas (por ejemplo: pytest -v --html=reporte.html)
### python -m pytest -v --html=reports/reporteEntregaFinal_Vx.html --self-contained-html (cambiar "x" por la version que se testear)
### Los reportes se guardan en la subcarpeta "reports"

### Capturas de pantalla - Evidencia
### Se guardan en formato .png dentro de la subcarpeta "capturas"

### Detalle de los tests

### Se testean login de usuarios, casos de exito y casos con error forzado (usuario o password inválido)

### Se testean las operaciones del inventario: Navegacion, ordenado de productos por nombre y por precio, agregado de productos, comprobacion de cantidades en carrito y eliminacion de productos.

### Se testean API Http requests: GET, POST, PUT, PATCH, DELETE utlizando diferentes origenes de datos (CSV y JSON). Se comprueban response codes y se creo una funcion parametrizada en la que se pasan los response.code esperados. En algunas ejecuciones se fuerzan response codes erróneos para continuar con la ejecución de tests

### Tecnicas auxiliares utilizadas

### Markers, Fixtures, Captura de pantalla y Logging
