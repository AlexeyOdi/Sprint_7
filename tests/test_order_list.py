import requests
import allure

class TestOrderList:

    @allure.title('Проверяем запрос списка заказов')
    def test_get_order_list(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        assert "orders" in response.text
