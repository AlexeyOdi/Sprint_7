import requests
import allure
import test_urls


class TestOrderList:

    @allure.title('Проверяем запрос списка заказов')
    def test_get_order_list(self):
        response = requests.get(test_urls.order_url)
        assert "orders" in response.text
