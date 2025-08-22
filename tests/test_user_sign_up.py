import allure
from urls import Urls
from helpers import UserRandomData

class TestUserSignUp:

    @allure.title('Создание пользователя')
    @allure.description('Создаем нового пользователя')
    def test_user_sign_up_true(self, sign_up_page):
        current_url, login_page_header_present = sign_up_page.create_user(UserRandomData.create_user_data())
        assert current_url == Urls.SIGN_IN_URL and login_page_header_present