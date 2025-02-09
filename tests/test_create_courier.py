import requests
import allure
import random
import string

class TestCreateCourier:

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

    @allure.title('Проверяем создание курьера с правильно заполненными обязательными полями')
    def test_create_courier_with_necessary_fields(self):
        #test = TestBaseClass()
        courier_data = self.generate_courier()
        del courier_data['first_name']
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)
        assert response.status_code == 201

    @allure.title('Проверяем создание курьера с правильно заполненными обязательными полями и именем')
    def test_create_courier_with_name(self):
        courier_data = self.generate_courier()
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = courier_data)
        assert response.status_code == 201

    @allure.title('Проверяем возникновение ошибки при создании двух одинаковых курьеров')
    def test_create_same_courier(self):
        courier_data = self.generate_courier()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)
        assert response.status_code == 409

    @allure.title('Проверяем возникновение ошибки при создании курьера без логина')
    def test_create_courier_without_login(self):
        courier_data = self.generate_courier()
        del courier_data['login']
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)
        assert response.status_code == 400

    @allure.title('Проверяем возникновение ошибки при создании курьера без пароля')
    def test_create_courier_without_password(self):
        courier_data = self.generate_courier()
        del courier_data['password']
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)
        assert response.status_code == 400

    @allure.title('Проверяем правильность текста в теле ответа при создании курьера')
    def test_successful_status_code_text(self):
        courier_data = self.generate_courier()
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)
        assert response.text == '{"ok":true}'







