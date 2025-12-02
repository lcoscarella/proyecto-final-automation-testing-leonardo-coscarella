import requests
import pytest
import pytest_check as check
import faker

from tests.conftest import api_base_url
from utils.api_ancillary import validate_api_response

fake = faker.Faker()

from tests.conftest import logger

# Esta clase llama a la clase UserWorkflow que contiene el flujo completo de testing de usuarios.
# Esta parametrizada para enviar distintos códigos de respuesta esperados y validar el comportamiento del flujo ante respuestas exitosas y fallidas.

class TestUserWorkflow:
    @pytest.mark.parametrize(
        "a,b,c,d,e",
        [
            (200, 201, 200, 200, 200), # todos exitosos
            (200, 301, 200, 300, 200), # algunos con error
            (300, 201, 200, 200, 400)  # algunos con error
        ]
    )
    def test_user_workflow(self,api_base_url, a, b, c, d, e):
        wf = UserWorkflow()
        wf.test_user_workflow(api_base_url,a, b, c, d, e)

class UserWorkflow():
    def test_user_workflow(self, api_base_url,getRespCode=200,postRespCode=201,putRespCode=200,patchRespCode=200,deleteRespCode=200):
        logger.info("Circuito completo de testing de usuario(s):")
        logger.info("1 - GET Users")
 
        response = requests.get(f"{api_base_url}users")
        data = validate_api_response(response,getRespCode,[],2.0)

        logger.info("2 - POST User")
        new_user = {
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number()
        }
        response = requests.post(f"{api_base_url}users", json=new_user)
        created_user = validate_api_response(response,postRespCode,[],2.0)

        logger.info("3 - PUT User")
        updated_user = {
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number()
        }

        response = requests.put(f"{api_base_url}users/1", json=updated_user)
        validated_updated_user = validate_api_response(response,putRespCode,[],2.0)

        logger.info("4 - PATCH User")
        patch_data = {
            "email": fake.email()
        }
        response = requests.patch(f"{api_base_url}users/1", json=patch_data)
        validated_patched_user = validate_api_response(response,patchRespCode,[],2.0)

        logger.info("5 - DELETE User")
        response = requests.delete(f"{api_base_url}users/1")
        validated_deleted_user = validate_api_response(response,deleteRespCode,[],2.0)
        
        logger.info("Flujo completo de usuario finalizado con éxito.")
