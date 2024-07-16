import allure
import requests
from data_answer import ResponseMessages
from generation_data import GenerationData
from register_new_courier import register_new_courier_and_return_login_password
from urls import Urls

class TestCreateCourier:
    @allure.title('Тест создания курьера')
    @allure.description('Регистрируем нового курьера и проверяем его создание')
    def test_create_new_courier(self):
        login = GenerationData().generation_email()
        password = GenerationData().generation_password()
        name = GenerationData().generation_name()
        response = requests.post(f'{Urls().url_main_page}{Urls().endpoint_create_courier}', json={
            "login": login,
            "password": password,
            "firstName": name
        })
        assert response.status_code == 201
        assert response.json()["ok"] == ResponseMessages.COURIER_CREATED_SUCCESS

    @allure.title('Тест создания двух одинаковых курьеров')
    @allure.description('Регистрируем уже существующего курьера и проверяем отображение ошибки')
    def test_create_duplicate_courier(self):
        login, password, name = register_new_courier_and_return_login_password()
        response = requests.post(f'{Urls().url_main_page}{Urls().endpoint_create_courier}', json={
            "login": login,
            "password": password,
            "firstName": name
        })
        assert response.status_code == 409
        assert response.json()["message"] == ResponseMessages.DUPLICATE_COURIER_ERROR

    @allure.title('Тест создания курьера без обязательных полей')
    @allure.description('Регистрируем курьера без обязательных полей и проверяем отображение ошибки')
    def test_create_courier_missing_fields(self):
        login = GenerationData().generation_email()
        password = GenerationData().generation_password()
        name = GenerationData().generation_name()
        payloads = [
            {"password": password, "firstName": name},
            {"login": login, "firstName": name}
        ]
        for payload in payloads:
            response = requests.post(f'{Urls().url_main_page}{Urls().endpoint_create_courier}', json=payload)
            assert response.status_code == 400
            assert response.json()["message"] == ResponseMessages.MISSING_FIELDS_ERROR
