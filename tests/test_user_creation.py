import allure
import pytest
from data.messg_names import ErrorNames
from data.messg_names import TokenNames

class TestUserCreation:

    @allure.title("Тесты для ручек 'Создание пользователя'")

    @allure.step("Создать уникального пользователя")
    def test_create_user(self, user_api):
        payload  = user_api.create_new_user_data()
        response = user_api.create_user_rqst(payload)
        assert response.status_code == 200 and TokenNames.login_success_token in response.json()

    @allure.step("Создать пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, user_api):
        payload = user_api.create_new_user_data()
        response = user_api.create_user_rqst(payload)
        response = user_api.create_user_rqst(payload)
        assert response.status_code == 403
        assert response.json()['message'] == ErrorNames.duplicate_login_err

    @allure.step("Создать пользователя и не заполнить одно из обязательных полей")
    @pytest.mark.parametrize('inpt', ["email", "password", "name"])
    def test_create_user_with_one_empty_inpt(self, user_api, inpt):
        payload = user_api.create_new_user_data()
        payload[inpt] = ''
        response = user_api.create_user_rqst(payload)
        assert response.status_code == 403
        assert response.json()['message'] == ErrorNames.empty_inpt_err

