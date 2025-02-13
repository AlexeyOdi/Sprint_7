import pytest
import random
import string

@pytest.fixture(scope = "function")
def generate_courier(request):

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    courier_data = {}
    request.cls.courier_data = courier_data

    courier_data['login'] = generate_random_string(10)
    courier_data['password'] = generate_random_string(10)
    courier_data['first_name'] = generate_random_string(10)

    return courier_data

@pytest.fixture(scope = "function")
def generate_courier_and_delete(request):

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    courier_data = {}
    request.cls.courier_data = courier_data
    courier_data['login'] = generate_random_string(10)
    courier_data['password'] = generate_random_string(10)
    courier_data['first_name'] = generate_random_string(10)
    return courier_data
    yield
    login_response_text = response.text
    requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{login_response_text[0]}')
