import pytest
import requests
import allure
from data_answer import ResponseMessages
from urls import Urls


class TestGetOrder:
    @allure.title('Тест получение списка заказов')
    @allure.description('Проверяем получение списка заказов и отображение кода статуса')
    def test_get_orders_list(self):
        response = requests.get(f'{Urls().url_main_page}{Urls().endpoint_get_orders}')
        assert response.status_code == 200
        assert response.json()[ResponseMessages.ORDERS_LIST_SUCCESS]
