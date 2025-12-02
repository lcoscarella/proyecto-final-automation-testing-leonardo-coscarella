import csv
import pathlib 
import json
import faker   

# Funciones para leer datos de login desde CSV  
def leer_csv_login(ruta_csv):
    casos = []
    with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        for fila in lector:
            username = fila['username']
            password = fila['password']
            valid = fila['valid'].strip().lower() == 'true'
            casos.append((username, password, valid))
    return casos

# Funciones para leer datos de login desde JSON
def leer_json_login(ruta_json):
    casos = []
    with open(ruta_json, newline='', encoding='utf-8') as jsonfile:
        datos = json.load(jsonfile)
        for fila in datos:
            username = fila['username']
            password = fila['password']
            valid = fila['valid']
            casos.append((username, password, valid))
    
    return casos

# Funciones para leer datos de login desde JSON y agregar datos falsos
def leer_json_y_fakes_login(ruta_json):
    casos = []
    with open(ruta_json, newline='', encoding='utf-8') as jsonfile:
        datos = json.load(jsonfile)
        for fila in datos:
            username = fila['username']
            password = fila['password']
            valid = fila['valid']
            casos.append((username, password, valid))

    fake = faker.Faker()
    for _ in range(5):
        username = fake.user_name()
        password = fake.password()
        valid = False
        casos.append((username, password, valid))

    return casos

if __name__ == "__main__":
    ruta_actual = pathlib.Path(__file__).parent
    ruta_csv = ruta_actual / 'login.csv'
    CASOS_LOGIN = leer_csv_login(ruta_csv)



CASOS_LOGIN = [
    ("standard_user","secret_sauce", True), # usuario válido, login exitoso    
    ("locked_out_user","secret_sauce", False), # usuario bloqueado, login inválido
    ("usuario_invalido","password_invalido", False), # usuario inválido, login inválido


]