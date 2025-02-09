import requests
import allure
import random
import string

class TestLoginCourier:

    def generate_random_string(self, length):

        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_courier(self):

        courier_data = {}

        courier_data['login'] = self.generate_random_string(10)
        courier_data['password'] = self.generate_random_string(10)
        courier_data['first_name'] = self.generate_random_string(10)

        return courier_data

    @allure.title('Проверяем вход в аккаунт курьера с правильно заполненными полями')
    def test_login_courier_with_necessary_fields(self):
        courier_data = self.generate_courier()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data)

        assert response.status_code == 200

    @allure.title('Проверяем вход в аккаунт курьера с несуществующим логином')
    def test_login_courier_with_wrong_login(self):
        courier_data = self.generate_courier()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)
        courier_data['login'] = 'Alexey'
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data)

        assert response.status_code == 404

    @allure.title('Проверяем вход в аккаунт курьера с несуществующим паролем')
    def test_login_courier_with_wrong_password(self):
        courier_data = self.generate_courier()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)
        courier_data['password'] = 'Alexey'
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data)

        assert response.status_code == 404

    @allure.title('Проверяем вход в аккаунт курьера без логина')
    def test_login_courier_without_login(self):
        courier_data = self.generate_courier()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)
        del courier_data['login']
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data)

        assert response.status_code == 400

    @allure.title('Проверяем, что при входе в аккаунт курьера в теле ответа приходит id')
    def test_id_in_response(self):
        courier_data = self.generate_courier()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data)

        assert 'id' in response.text