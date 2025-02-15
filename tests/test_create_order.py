import requests
import allure
import pytest
import test_urls
from test_data import color_data, order_data


class TestCreateOrder:

    @allure.title('Проверяем возможность создания заказа с разными параметрами цвета')
    @pytest.mark.parametrize("value", color_data)
    def test_order(self, value):
        order_data["color"] = value
        response = requests.post(test_urls.main_url+test_urls.order_url, data=order_data)
        assert response.status_code == 201 and "track" in response.text

    @allure.title('Проверяем что при создании заказа в теле ответа присутствует трек-номер')
    def test_track_id_in_order(self):
        order_data["color"] = color_data[0]
        response = requests.post(test_urls.main_url+test_urls.order_url, data=order_data)
        assert "track" in response.text