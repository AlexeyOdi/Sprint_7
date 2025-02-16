import allure
import test_data
import pytest

class TestLoginCourier:

    @allure.title('Проверяем вход в аккаунт курьера с правильно заполненными полями')
    @pytest.mark.usefixtures('delete_courier')
    def test_login_courier_with_necessary_fields(self):
        assert self.response.status_code == 200 and "id" in self.response.text

    @allure.title('Проверяем вход в аккаунт курьера с несуществующим логином')
    @pytest.mark.f_data('login')
    def test_login_courier_with_wrong_login(self, delete_courier):
        assert self.response.status_code == 404 and test_data.login_message_unsuccess in self.response.text


    @allure.title('Проверяем вход в аккаунт курьера с несуществующим паролем')
    @pytest.mark.f_data('password')
    def test_login_courier_with_wrong_password(self, delete_courier):
        assert self.response.status_code == 404 and test_data.login_message_unsuccess in self.response.text

    @allure.title('Проверяем вход в аккаунт курьера без логина')
    @pytest.mark.f_data('delete login')
    def test_login_courier_without_login(self, delete_courier):
        assert self.response.status_code == 400 and test_data.login_message_without_field in self.response.text

    @pytest.mark.usefixtures("delete_courier")
    @allure.title('Проверяем, что при входе в аккаунт курьера в теле ответа приходит id')
    def test_id_in_response(self):
        assert 'id' in self.response.text
