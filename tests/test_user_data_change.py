import allure
import pytest
from faker import Faker
from data.messg_names import ErrorNames
from data.messg_names import TokenNames

class TestUserDataChange:
    
    @allure.title("Изменение данных пользователя")
    @allure.step("с авторизацией, меняем email")
    @pytest.mark.parametrize('inpt_e', ["email"])
    def test_change_auth_user_data_email(self, user_api, inpt_e):
       
        fake = Faker("en_US")
        payload  = user_api.create_new_user_data()
        response_t = user_api.get_token(payload, TokenNames.login_success_token)
        payload[inpt_e] = fake.email()
        response = user_api.user_data_change_rqst(payload, response_t)
        assert response.status_code == 200 and response.json()['success'] == True




    @allure.step("с авторизацией, меняем password")
    @pytest.mark.parametrize('inpt_p', ["password"])
    def test_change_auth_user_data_pass(self, user_api, inpt_p):
       
        fake = Faker("en_US")
        payload  = user_api.create_new_user_data()
        response_t = user_api.get_token(payload, TokenNames.login_success_token)
        payload[inpt_p] = fake.password()
        response = user_api.user_data_change_rqst(payload, response_t)
        assert response.status_code == 200 and response.json()['success'] == True



    @allure.step("Без авторизациии, меняем email")
    @pytest.mark.parametrize('inpt_e', ["email"])
    def test_change_not_auth_user_data_email(self, user_api, inpt_e):
       
        fake = Faker("en_US")
        payload  = user_api.create_new_user_data()
        payload[inpt_e] = fake.email()
        response = user_api.user_data_change_rqst(payload, TokenNames.login_success_token)
        assert response.status_code == 401
        assert response.json()['message'] == ErrorNames.you_should_be_aut_err


    @allure.step("Без авторизации, меняем password")
    @pytest.mark.parametrize('inpt_p', ["password"])
    def test_change_not_auth_user_data_pass(self, user_api, inpt_p):
       
        fake = Faker("en_US")
        payload  = user_api.create_new_user_data()
        payload[inpt_p] = fake.password()
        response = user_api.user_data_change_rqst(payload, TokenNames.login_success_token)
        assert response.status_code == 401 
        assert response.json()['message'] == ErrorNames.you_should_be_aut_err


