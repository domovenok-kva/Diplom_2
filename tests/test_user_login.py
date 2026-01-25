import allure
import pytest
from data.messg_names import ErrorNames
from data.messg_names import TokenNames

class TestUserLogin:

    @allure.title("Логин пользователя")
    @allure.step("Логин под существующим пользователем")
    def test_exist_user_login(self, user_api):
        payload  = user_api.create_new_user_data()
        response = user_api.create_user_rqst(payload)
        response = user_api.login_exist_user_rqst(payload)
        response_t = user_api.get_token(payload, TokenNames.login_success_token)
        user_api.user_data_delete_rqst(response_t)
        assert response.status_code == 200 and TokenNames.login_success_token in response.json()


    @allure.step("Логин с неверным логином и паролем")
    @pytest.mark.parametrize('inpt', ["email", "password"])
    def test_login_whith_not_correct_data(self, user_api, inpt):
        payload = user_api.create_new_user_data()
        response = user_api.create_user_rqst(payload)
        response_t = user_api.get_token(payload, TokenNames.login_success_token)
        payload[inpt] = 'invalid_data'
        response = user_api.login_exist_user_rqst(payload)
        user_api.user_data_delete_rqst(response_t)       
        assert response.status_code == 401
        assert response.json()['message'] == ErrorNames.incorrect_email_or_password_err