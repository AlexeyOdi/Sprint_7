import requests
import allure
import helpers
import test_urls
import test_data

class TestLoginCourier:

    @allure.title('Проверяем вход в аккаунт курьера с правильно заполненными полями')
    def test_login_courier_with_necessary_fields(self):
        courier_data = helpers.generate_courier()
        requests.post(test_urls.main_url+test_urls.create_courier_url, data=courier_data)
        response = requests.post(test_urls.main_url+test_urls.login_courier_url, data=courier_data)

        assert response.status_code == 200 and "id" in response.text
        helpers.delete_courier(response.text)

    @allure.title('Проверяем вход в аккаунт курьера с несуществующим логином')
    def test_login_courier_with_wrong_login(self):
        courier_data = helpers.generate_courier()
        requests.post(test_urls.main_url+test_urls.create_courier_url, data=courier_data)
        courier_data['login'] = 'Alexey'
        response = requests.post(test_urls.main_url+test_urls.login_courier_url, data=courier_data)

        assert response.status_code == 404 and test_data.login_message_unsuccess in response.text
        helpers.delete_courier(response.text)

    @allure.title('Проверяем вход в аккаунт курьера с несуществующим паролем')
    def test_login_courier_with_wrong_password(self):
        courier_data = helpers.generate_courier()
        requests.post(test_urls.main_url+test_urls.create_courier_url, data=courier_data)
        courier_data['password'] = 'Alexey'
        response = requests.post(test_urls.main_url+test_urls.login_courier_url, data=courier_data)

        assert response.status_code == 404 and test_data.login_message_unsuccess in response.text
        helpers.delete_courier(response.text)

    @allure.title('Проверяем вход в аккаунт курьера без логина')
    def test_login_courier_without_login(self):
        courier_data = helpers.generate_courier()
        requests.post(test_urls.main_url+test_urls.create_courier_url, data=courier_data)
        del courier_data['login']
        response = requests.post(test_urls.main_url+test_urls.login_courier_url, data=courier_data)

        assert response.status_code == 400 and test_data.login_message_without_field in response.text
        helpers.delete_courier(response.text)

    @allure.title('Проверяем, что при входе в аккаунт курьера в теле ответа приходит id')
    def test_id_in_response(self):
        courier_data = helpers.generate_courier()
        requests.post(test_urls.main_url+test_urls.create_courier_url, data=courier_data)
        response = requests.post(test_urls.main_url+test_urls.login_courier_url, data=courier_data)

        assert 'id' in response.text
        helpers.delete_courier(response.text)
