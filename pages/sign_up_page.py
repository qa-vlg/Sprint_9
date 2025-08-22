import allure
from pages.base_page import BasePage
from locators.locators import Locators

class SignUpPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Нажимаем кнопку создания аккаунта')
    def navigate_to_sign_up_page(self):
        self.click_on_element(Locators.TOP_CREATE_ACCOUNT_BUTTON)

    @allure.step('Заполняем поле Имя')
    def enter_first_name(self, first_name):
        self.enter_text(Locators.FIRST_NAME_INPUT_FIELD, first_name)

    @allure.step('Заполняем поле Фамилия')
    def enter_last_name(self, last_name):
        self.enter_text(Locators.LAST_NAME_INPUT_FIELD, last_name)

    @allure.step('Заполняем поле user_name')
    def enter_user_name(self, user_name):
        self.enter_text(Locators.USER_NAME_INPUT_FIELD, user_name)

    @allure.step('Заполняем поле emai')
    def enter_email(self, email):
        self.enter_text(Locators.EMAIL_INPUT_FIELD, email)

    @allure.step('Заполняем поле password')
    def enter_pwd(self, pwd):
        self.enter_text(Locators.PWD_INPUT_FIELD, pwd)

    @allure.step('Нажимаем кнопку создать аккаунт')
    def click_create_account(self):
        self.click_on_element(Locators.MID_CREATE_ACCOUNT_BUTTON)

    @allure.step('Создаем аккаунт')
    def create_user(self, user_data):
        self.enter_first_name(user_data["first_name"])
        self.enter_last_name(user_data["last_name"])
        self.enter_user_name(user_data["user_name"])
        self.enter_email(user_data["email"])
        self.enter_pwd(user_data["password"])
        self.click_create_account()
        self.wait_for_element_to_be_present(Locators.ENTER_SITE_HEADER)
        current_url = self.get_page_url()
        return current_url, self.element_is_present(Locators.ENTER_SITE_HEADER)