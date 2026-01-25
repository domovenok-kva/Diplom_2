import allure
from faker import Faker
from data.messg_names import ErrorNames
from data.messg_names import TokenNames

class TestOrderCreation:

    @allure.title("Тесты для ручек 'Создание заказа'")
    @allure.step("С авторизацией и с ингредиентами")
    def test_order_creation_with_auth(self, user_api, order_api):
        payload  = user_api.create_new_user_data()
        response_t = user_api.get_token(payload, TokenNames.login_success_token)
        ingridients = order_api.ingridients()
        response = order_api.create_order_rqst(ingridients, response_t)
        user_api.user_data_delete_rqst(response_t)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.step("без авторизации")
    @allure.description("Баг: Приложение позволяет создать заказ без авторизации")
    def test_order_creation_no_auth(self, order_api):
       ingridients = order_api.ingridients()
       response  = order_api.create_order_rqst(ingridients, "")
       assert response.json()['success'] == True   

    @allure.step("Без ингредиентов")
    def test_order_creation_without_ingridients(self, user_api, order_api):
        payload  = user_api.create_new_user_data()
        response_t = user_api.get_token(payload, TokenNames.login_success_token)
        ingridients = ''
        response = order_api.create_order_rqst(ingridients, response_t)
        user_api.user_data_delete_rqst(response_t)
        assert response.status_code == 400 
        assert response.json()['message'] == ErrorNames.no_ingridients_err

    @allure.step("с неверным хешем ингредиентов")
    def test_invalid_hesh(self, user_api, order_api):
        fake = Faker("en_US")
        payload  = user_api.create_new_user_data()
        response_t = user_api.get_token(payload, TokenNames.login_success_token)
        invalid_ing = fake.ipv6()
        response = order_api.create_order_rqst(invalid_ing, response_t)
        user_api.user_data_delete_rqst(response_t)
        assert response.status_code == 500
  

