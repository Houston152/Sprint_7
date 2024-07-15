import allure
import requests
from generation_data import GenerationData
from register_new_courier import register_new_courier_and_return_login_password
from urls import Urls

class TestCreateCourier:
    @allure.description('Регистрируем нового курьера и проверяем его создание')
    def test_create_new_courier(self):
        login = GenerationData().generation_email()
        password = GenerationData().generation_password()
        name = GenerationData().generation_name()
        response = requests.post(f'{Urls().url_main_page}api/v1/courier', json={
            "login": login,
            "password": password,
            "firstName": name
        })
        assert response.status_code == 201
        assert response.json()["ok"] == True

    @allure.description('Регистрируем уже существующего курьера и проверяем отображение ошибки')
    def test_create_duplicate_courier(self):
        login, password, name = register_new_courier_and_return_login_password()
        response = requests.post(f'{Urls().url_main_page}api/v1/courier', json={
            "login": login,
            "password": password,
            "firstName": name
        })
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

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
            response = requests.post(f'{Urls().url_main_page}api/v1/courier', json=payload)
            assert response.status_code == 400
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
