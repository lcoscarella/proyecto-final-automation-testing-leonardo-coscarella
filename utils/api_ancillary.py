import requests
import pytest_check as check

# API variables
api_url = "https://jsonplaceholder.typicode.com/"

def get_users():
    response = requests.get(f"{api_url}users")
    print(response.status_code)

    assert response.status_code == 200, "Error: No se pudo obtener la lista de usuarios"

    data = response.json()
    print(data)

def post_users():
    payload = {
        "name": "Juan Perez",
        "username": "jperez",
        "email": "jperez@algo.com"}

    response = requests.post(f"{api_url}users", json=payload)
    print(response.status_code)
    data = response.json()
    print(data)

def validate_api_response(response, expected_status,expected_fields=None,max_time=1.0): 
    # Funcion helper para validar respuestas de APIs
    # Dejo comentados los asserts en caso de que se necesiten, pero usamos check.equal/is_true para seguir con la ejecucion de todos los tests aunque falle uno

    # Nivel 1: Status
    check.equal(response.status_code, expected_status, f"Error: Se esperaba el estado {expected_status} pero se obtuvo {response.status_code}")
    #assert response.status_code == expected_status, f"Error: Se esperaba el estado {expected_status} pero se obtuvo {response.status_code}"


    # Nivel 2: Headers
    if expected_status != 204:
        check.is_true('application/json' in response.headers.get('Content-Type',''), "Error: El tipo de contenido no es JSON")
        #assert 'application/json' in response.headers.get('Content-Type',''), "Error: El tipo de contenido no es JSON"
    
    # Nivel 3-4: Estructura y contenido
    if expected_fields and response.text:
        body = response.json()
        check.is_true(expected_fields <= set(body.keys()), f"Error: La respuesta no contiene los campos esperados {expected_fields}") 
        #assert expected_fields <= set(body.keys()), f"Error: La respuesta no contiene los campos esperados {expected_fields}"

    # Nivel 5: Tiempo de respuesta
    check.is_true(response.elapsed.total_seconds() < max_time, f"Error: El tiempo de respuesta {response.elapsed.total_seconds()} excede el máximo permitido de {max_time} segundos")
    #assert response.elapsed.total_seconds() < max_time, f"Error: El tiempo de respuesta {response.elapsed.total_seconds()} excede el máximo permitido de {max_time} segundos"
    return response.json() if response.text else {}

