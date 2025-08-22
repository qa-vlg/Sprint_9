import allure
from urls import Urls

class TestUserLogin:

    @allure.title('Логин пользователя')
    @allure.description('Логин существующего пользователя')
    def test_user_login_valid_data_true(self, user_login):
        current_url, exit_button_present = user_login
        assert current_url == Urls.RECIPES_PAGE_URL and exit_button_present