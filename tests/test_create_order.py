import pytest
import requests
import allure
from data_answer import ResponseMessages
from generation_data import StorageData
from urls import Urls


class TestCreateOrder:
    @allure.title('Тест создания нового заказа')
    @allure.description('Проверяем создание нового заказа и отображение кода статуса и сообщения с номером заказа')
    @pytest.mark.parametrize("colors", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([])
    ])
    def test_create_order(self, colors):
        StorageData().order_data["color"] = colors
        response = requests.post(f'{Urls().url_main_page}{Urls().endpoint_create_order}', json=StorageData().order_data)
        assert response.status_code == 201
        assert response.json()[ResponseMessages.ORDER_CREATED_SUCCESS]
