import pytest
from api.user_api import UserAPI
from api.order_api import OrderApi

@pytest.fixture()
def user_api():
    user_api = UserAPI()
    yield user_api
   
@pytest.fixture()
def order_api():
    order_api = OrderApi()
    return order_api
   