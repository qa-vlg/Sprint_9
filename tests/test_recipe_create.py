import allure
import pytest
from data import RecipeData

class TestRecipeCreate:

    @allure.title('Создание рецепта')
    @allure.description('Создаем рецепт')
    @pytest.mark.parametrize("recipe_data", [(RecipeData.salad)])
    def test_create_recipe_true(self, recipe_data, recipe):
        expected_recipe_name = RecipeData.salad["name"]
        recipe_page = recipe
        actual_recipe_name = recipe_page.create_recipe(recipe_data)
        assert actual_recipe_name == expected_recipe_name