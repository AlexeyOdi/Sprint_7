import requests
import allure
import pytest

class TestCreateOrder:

    order_data = {
        "firstName": "Алексей",
        "lastName": "Алексеев",
        "address": "Воронцовский 20",
        "metroStation": "4",
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-02-23T21:00:00.000Z",
        "comment": "",
    }

    test_data = [
        (["",""]),
        (["BLACK",""]),
        (["GRAY",""]),
        (["BLACK","GRAY"])
    ]

    @allure.title('Проверяем возможность создания заказа с разными параметрами цвета')
    @pytest.mark.parametrize("value", test_data)
    def test_order(self, value):
        self.order_data["color"] = value
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=self.order_data)
        assert response.status_code == 201

    @allure.title('Проверяем что при создании заказа в теле ответа присутствует трек-номер')
    def test_track_id_in_order(self):
        self.order_data["color"] = self.test_data[0]
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=self.order_data)
        assert "track" in response.text