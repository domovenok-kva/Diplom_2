import allure
import requests
from faker import Faker
from data.urls_for_test import UrlsForTest

class UserAPI:
        
    @allure.step("Создание пользователя")
    def create_new_user_data(self):
        fake = Faker("en_US")
        new_user_data = { 'email': fake.email(), 'password': fake.password(), 'name': fake.name()}
        return new_user_data
    

    @allure.step("Запрос на создание пользователя")
    def create_user_rqst(self, payload):
        return requests.post(UrlsForTest.create_user_url, data = payload)
    
    @allure.step("Запрос на залогин зарегистрированного пользователя")
    def login_exist_user_rqst(self, payload):
        return requests.post(UrlsForTest.user_login_url, data = payload)
    
    @allure.step("Запрос на изменение данных пользователя")
    def user_data_change_rqst(self, payload, token):
        headers = {'authorization' : token}
        return requests.patch(UrlsForTest.user_data_url, json = payload, headers = headers)
    
    @allure.step("Удаление пользователя")
    def user_data_delete_rqst(self, token):
        headers = {'authorization' : token}
        return requests.delete(UrlsForTest.user_del, headers = headers)
    
    @allure.step("Получение токена")
    def get_token(self, payload, token):
        user_api = UserAPI()
        response = user_api.create_user_rqst(payload)
        response = user_api.login_exist_user_rqst(payload)
        response_jsn = response.json()
        token_rssp = response_jsn.get(token)
        return  token_rssp


    

