import requests
import allure
import pytest
import test_urls
import test_data

@pytest.mark.usefixtures("generate_courier")
class TestLoginCourier:

    @allure.title('Проверяем вход в аккаунт курьера с правильно заполненными полями')
    def test_login_courier_with_necessary_fields(self):
        requests.post(test_urls.create_courier_url, data=self.courier_data)
        response = requests.post(test_urls.login_courier_url, data=self.courier_data)

        assert response.status_code == 200 and "id" in response.text

    @allure.title('Проверяем вход в аккаунт курьера с несуществующим логином')
    def test_login_courier_with_wrong_login(self):
        requests.post(test_urls.create_courier_url, data=self.courier_data)
        self.courier_data['login'] = 'Alexey'
        response = requests.post(test_urls.login_courier_url, data=self.courier_data)

        assert response.status_code == 404 and test_data.login_message_unsuccess in response.text

    @allure.title('Проверяем вход в аккаунт курьера с несуществующим паролем')
    def test_login_courier_with_wrong_password(self):
        requests.post(test_urls.create_courier_url, data=self.courier_data)
        self.courier_data['password'] = 'Alexey'
        response = requests.post(test_urls.login_courier_url, data=self.courier_data)

        assert response.status_code == 404 and test_data.login_message_unsuccess in response.text

    @allure.title('Проверяем вход в аккаунт курьера без логина')
    def test_login_courier_without_login(self):
        requests.post(test_urls.create_courier_url, data=self.courier_data)
        del self.courier_data['login']
        response = requests.post(test_urls.login_courier_url, data=self.courier_data)

        assert response.status_code == 400 and test_data.login_message_without_field in response.text

    @allure.title('Проверяем, что при входе в аккаунт курьера в теле ответа приходит id')
    def test_id_in_response(self):
        requests.post(test_urls.create_courier_url, data=self.courier_data)
        response = requests.post(test_urls.login_courier_url, data=self.courier_data)

        assert 'id' in response.text