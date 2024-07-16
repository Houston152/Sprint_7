import requests
import allure
from data_answer import ResponseMessages
from generation_data import GenerationData
from register_new_courier import register_new_courier_and_return_login_password
from urls import Urls

class TestAuthorizationCourier:
    @allure.title('Тест авторизации курьера')
    @allure.description('Проверяем авторизацию курьера с валидными данными')
    def test_authorization_courier(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        response = requests.post(f'{Urls().url_main_page}{Urls().endpoint_authorization_courier}', json={
            "login": login,
            "password": password
        })
        assert response.status_code == 200
        assert response.json()[ResponseMessages.AUTHORIZATION_SUCCESS]

    @allure.title('Тест авторизации курьера без обязательных полей')
    @allure.description('Авторизуемся без обязательных полей и проверяем отображение ошибки с кодом статуса')
    def test_authorization_missing_fields(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        payloads = [
            {"password": password},
            {"login": login},
            {}
        ]
        for payload in payloads:
            response = requests.post(f'{Urls().url_main_page}{Urls().endpoint_authorization_courier}', json=payload)
            assert response.status_code == 400
            assert response.json()["message"] == ResponseMessages.AUTHORIZATION_MISSING_FIELDS_ERROR

    @allure.title('Тест авторизации курьера с невалидными данными')
    @allure.description('Авторизуемся с невалидными данными и проверяем отображение ошибки с кодом статуса')
    def test_authorization_invalid_login_or_password(self):
        login = GenerationData().generation_email()
        password = GenerationData().generation_password()
        response = requests.post(f'{Urls().url_main_page}{Urls().endpoint_authorization_courier}', json={
            "login": login,
            "password": password
        })
        assert response.status_code == 404
        assert response.json()["message"] == ResponseMessages.AUTHORIZATION_INVALID_CREDENTIALS_ERROR
