import requests
import allure
from generation_data import GenerationData
from register_new_courier import register_new_courier_and_return_login_password
from urls import Urls

class TestAuthorizationCourier:
    @allure.description('Авторизация курьера')
    def test_authorization_courier(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        response = requests.post(f'{Urls().url_main_page}api/v1/courier/login', json={
            "login": login,
            "password": password
        })
        assert response.status_code == 200
        assert response.json()["id"]

    @allure.description('Авторизация курьера без обязательных полей')
    def test_authorization_missing_fields(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        payloads = [
            {"password": password},
            {"login": login},
            {}
        ]
        for payload in payloads:
            response = requests.post(f'{Urls().url_main_page}api/v1/courier/login', json=payload)
            assert response.status_code == 400
            assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.description('Авторизация курьера с невалидными данными')
    def test_authorization_invalid_login_or_password(self):
        login = GenerationData().generation_email()
        password = GenerationData().generation_password()
        response = requests.post(f'{Urls().url_main_page}api/v1/courier/login', json={
            "login": login,
            "password": password
        })
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
