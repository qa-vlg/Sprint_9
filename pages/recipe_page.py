import allure
import random
from helpers import FilePath
from pages.base_page import BasePage
from locators.locators import Locators


class RecipePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем нв вкладку Создания рецепта')
    def navigate_to_recipe_tab(self):
        self.click_on_element(Locators.RECIPE_TAB)

    @allure.step('Заполняем название рецепта')
    def fill_in_recipe_name(self, recipe_name):
        self.enter_text(Locators.RECIPE_NAME_INPUT, recipe_name)
    
    @allure.step('Добавляем ингредиенты')
    def add_ingredients(self, ingredients_data):
        for ingredient in ingredients_data:
            self.enter_text(Locators.RECIPE_INGREDIENTS_INPUT, ingredient)
            self.wait_for_element_to_be_present(Locators.RECIPE_SUGGESTED_INGREDIENTS)
            self.click_on_element(Locators.RECIPE_SUGGESTED_INGREDIENT)
            self.wait_for_element_to_disapear(Locators.RECIPE_SUGGESTED_INGREDIENTS)
            self.add_ingredient_weight()
            self.click_on_element(Locators.RECIPE_ADD_INGREDIENT_BUTTON)

    @allure.step('Добавляем колличество ингредиента')
    def add_ingredient_weight(self):
        self.enter_text(Locators.RECIPE_INGREDIENTS_WEIGHT_INPUT, str(random.randint(10, 100)))

    @allure.step('Задаем время готовки')
    def set_cooking_time(self):
        self.enter_text(Locators.RECIPE_COOKING_TIME_INPUT, str(random.randint(10, 100)))

    @allure.step('Добавляем описание рецепта')
    def add_recipe_description(self, recipe_description):
        self.enter_text(Locators.RECIPE_DESCRIPTION_INPUT, recipe_description)

    @allure.step('Добавляем фото рецепта')
    def add_recipe_image(self, file):
        self.upload_photo(Locators.RECIPE_UPLOAD_PHOTO_BUTTON, file)

    @allure.step('Нажимаем Создать рецепт')
    def click_create_recipe_button(self):
        self.click_on_element(Locators.RECIPE_CREATE_BUTTON)

    @allure.step('Создаем рецепт')
    def create_recipe(self, ingredients_data):
        self.fill_in_recipe_name(ingredients_data["name"])
        self.add_ingredients(ingredients_data["ingredients"])
        self.set_cooking_time()
        self.scroll_to_the_bottom()
        self.add_recipe_description(ingredients_data["recipe_description"])
        self.add_recipe_image(FilePath.get_file_path(ingredients_data["image"]))
        self.click_create_recipe_button()
        return self.get_page_element_text(Locators.RECIPE_CARD_NAME)