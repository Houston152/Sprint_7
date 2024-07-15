import pytest
import requests
import allure
from generation_data import StorageData
from urls import Urls


class TestCreateOrder:
    @allure.description('Создание нового заказа')
    @pytest.mark.parametrize("colors", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([])
    ])
    def test_create_order(self, colors):
        StorageData().order_data["color"] = colors
        response = requests.post(f'{Urls().url_main_page}api/v1/orders', json=StorageData().order_data)
        assert response.status_code == 201
        assert response.json()["track"]

    @allure.description('Получение списка заказов')
    def test_get_orders_list(self):
        response = requests.get(f'{Urls().url_main_page}api/v1/orders')
        assert response.status_code == 200
        assert response.json()["orders"]
