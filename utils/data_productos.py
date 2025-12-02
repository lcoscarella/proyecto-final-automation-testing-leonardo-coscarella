import json

def leer_datos_productos(ruta_archivo):
    with open(ruta_archivo, 'r',encoding='utf-8') as archivo:
        productos = json.load(archivo)
    
    nombres = [producto['nombre'] for producto in productos]

    return nombres

if __name__ == "__main__":
    ruta = 'data/productos.json'
    productos = leer_datos_productos(ruta)
    print(productos)


