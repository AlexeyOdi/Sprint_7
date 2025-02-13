import requests
import allure
import pytest
import test_urls
import test_data

@pytest.mark.usefixtures("generate_courier")
class TestCreateCourier:

    @allure.title('Проверяем создание курьера с правильно заполненными обязательными полями')
    def test_create_courier_with_necessary_fields(self):
        del self.courier_data['first_name']
        response = requests.post(test_urls.create_courier_url, data=self.courier_data)
        assert response.status_code == 201 and test_data.success_create_courier in response.text

    @allure.title('Проверяем создание курьера с правильно заполненными обязательными полями и именем')
    def test_create_courier_with_name(self):
        response = requests.post(test_urls.create_courier_url, data=self.courier_data)
        assert response.status_code == 201 and test_data.success_create_courier in response.text

    @allure.title('Проверяем возникновение ошибки при создании двух одинаковых курьеров')
    def test_create_same_courier(self):
        requests.post(test_urls.create_courier_url, data=self.courier_data)
        response = requests.post(test_urls.create_courier_url, data=self.courier_data)
        assert response.status_code == 409 and test_data.repetitive_login_message in response.text
        print(response.text)

    @allure.title('Проверяем возникновение ошибки при создании курьера без логина')
    def test_create_courier_without_login(self):
        del self.courier_data['login']
        response = requests.post(test_urls.create_courier_url, data=self.courier_data)
        assert response.status_code == 400 and test_data.unsuccessful_create_courier in response.text

    @allure.title('Проверяем возникновение ошибки при создании курьера без пароля')
    def test_create_courier_without_password(self):
        del self.courier_data['password']
        response = requests.post(test_urls.create_courier_url, data=self.courier_data)
        assert response.status_code == 400 and test_data.unsuccessful_create_courier in response.text

    @allure.title('Проверяем правильность текста в теле ответа при создании курьера')
    def test_successful_status_code_text(self):
        response = requests.post(test_urls.create_courier_url, data=self.courier_data)
        assert response.text == test_data.success_create_courier







