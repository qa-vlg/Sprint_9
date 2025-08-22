import allure
from pages.base_page import BasePage
from locators.locators import Locators

class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем кнопку Логина')
    def navigate_to_login_page(self):
        self.click_on_element(Locators.TOP_ENTER_BUTTON)

    @allure.step('Заполняем поле email')
    def enter_email(self, email):
        self.enter_text(Locators.EMAIL_INPUT_FIELD, email)

    @allure.step('Заполняем поле password')
    def enter_pwd(self, pwd):
        self.enter_text(Locators.PWD_INPUT_FIELD, pwd)

    @allure.step('Нажимаем кнопку Войти')
    def click_enter(self):
        self.click_on_element(Locators.MID_ENTER_BUTTON)

    @allure.step('Осуществляем логин Пользователя')
    def user_login(self, email, pwd):
        self.enter_email(email)
        self.enter_pwd(pwd)
        self.click_enter()
        self.wait_for_element_to_be_present(Locators.TOP_EXIT_BUTTON)
        current_url = self.get_page_url()
        return current_url, self.element_is_present(Locators.TOP_EXIT_BUTTON)