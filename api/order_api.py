import allure
import requests
from data.urls_for_test import UrlsForTest

class OrderApi:


    @allure.step("Получение списка ингридиентов")
    def ingridients_list_get(self):
        return requests.get(UrlsForTest.ingidients_list_url)
    
    def ingridients(self):
        order_api = OrderApi()
        response = order_api.ingridients_list_get()
        return response.json()['data']

    @allure.step("Запрос на создание заказа")
    def create_order_rqst(self, ingridients, token):
        headers = {'authorization' : token}
        payload = {"ingredients": ingridients}
        return requests.post(UrlsForTest.create_order_url, json = payload, headers = headers)
    
    @allure.step("Запрос на получение заказов пользователя")
    def users_orders_get_rqst(self, token):
        headers = {'authorization' : token}
        return requests.get(UrlsForTest.list_of_orders_url, headers = headers)