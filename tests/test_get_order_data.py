import allure
from data.messg_names import ErrorNames
from data.messg_names import TokenNames

class TestGetOrderData:

    @allure.title("Получение заказов конкретного пользователя")
    @allure.step("авторизованный пользователь")
    def test_order_of_auth_user_get_data(self, user_api, order_api):
        payload  = user_api.create_new_user_data()
        response_t = user_api.get_token(payload, TokenNames.login_success_token)
        ingridients = order_api.ingridients()
        response = order_api.create_order_rqst(ingridients, response_t)
        response = order_api.users_orders_get_rqst(response_t)
        user_api.user_data_delete_rqst(response_t)
        assert response.json()['success'] == True   

    @allure.step("неавторизованный пользователь")
    def test_order_no_auth_user_get_data(self, order_api):
        response_t = '' 
        ingridients = order_api.ingridients()
        response = order_api.create_order_rqst(ingridients, response_t)
        response = order_api.users_orders_get_rqst(response_t)
        assert response.status_code == 401 
        assert response.json()['message'] == ErrorNames.you_should_be_aut_err  