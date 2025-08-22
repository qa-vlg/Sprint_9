from selenium.webdriver.common.by import By

class Locators:

    # autorization 
    TOP_ENTER_BUTTON = (By.XPATH, ".//*[contains(@class, 'styles_menuLink') and text()='Войти']")
    TOP_CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//*[contains(@class, 'styles_menuButton') and text()='Создать аккаунт']")

    # account create page
    REGISTRATION_PAGE_HEADER = (By.XPATH, ".//*[contains(@class, 'styles_title') and text()='Регистрация']")
    FIRST_NAME_INPUT_FIELD = (By.XPATH, ".//*[contains(@class, 'styles_inputField') and @name='first_name']")
    LAST_NAME_INPUT_FIELD = (By.XPATH, ".//*[contains(@class, 'styles_inputField') and @name='last_name']")
    USER_NAME_INPUT_FIELD = (By.XPATH, ".//*[contains(@class, 'styles_inputField') and @name='username']")
    EMAIL_INPUT_FIELD = (By.XPATH, ".//*[contains(@class, 'styles_inputField') and @name='email']") ### same for login form
    PWD_INPUT_FIELD = (By.XPATH, ".//*[contains(@class, 'styles_inputField') and @name='password']") ### same for login form
    MID_CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//*[contains(@class, 'style_button') and text()='Создать аккаунт']")

    # user login page
    ENTER_SITE_HEADER = (By.XPATH, ".//*[contains(@class, 'styles_title') and text()='Войти на сайт']")
    MID_ENTER_BUTTON = (By.XPATH, ".//*[contains(@class, 'styles_button') and text()='Войти']")
    TOP_EXIT_BUTTON = (By.XPATH, ".//*[contains(@class, 'styles_menuLink') and text()='Выход']")

    # recipe page
    RECIPE_TAB = (By.XPATH, ".//*[contains(@class, 'style_nav__link') and text()='Создать рецепт']")
    RECIPE_PAGE_HEADER = (By.XPATH, ".//*[contains(@class, 'styles_title') and text()='Создание рецепта']")
    RECIPE_NAME_INPUT = (By.XPATH, ".//*[contains(@class, 'styles_inputLabelText') and text()='Название рецепта']/following-sibling::input")
    RECIPE_INGREDIENTS_INPUT = (By.XPATH, ".//*[contains(@class, 'styles_inputLabelText') and text()='Ингредиенты']/following-sibling::input")
    RECIPE_INGREDIENTS_WEIGHT_INPUT = (By.XPATH, ".//*[contains(@class, 'styles_ingredientsAmountInput')]//input")
    RECIPE_SUGGESTED_INGREDIENTS = (By.XPATH, ".//*[contains(@class, 'styles_ingredientsInputs')]/div[3]")
    RECIPE_SUGGESTED_INGREDIENT = (By.XPATH, ".//*[contains(@class, 'styles_ingredientsInputs')]/div[3]//div[1]")
    RECIPE_ADD_INGREDIENT_BUTTON = (By.XPATH, ".//*[contains(@class, 'styles_ingredientAdd') and text()='Добавить ингредиент']")
    RECIPE_COOKING_TIME_INPUT = (By.XPATH, ".//*[contains(@class, 'styles_inputLabelText') and text()='Время приготовления']/following-sibling::input")
    RECIPE_DESCRIPTION_INPUT = (By.XPATH, ".//div[text()='Описание рецепта']/following-sibling::textarea")
    RECIPE_UPLOAD_PHOTO_BUTTON = (By.XPATH, ".//input[contains(@class, 'styles_fileInput') and @type='file']")
    RECIPE_CREATE_BUTTON = (By.XPATH, ".//*[contains(@class, 'style_button') and text()='Создать рецепт']")
    RECIPE_CARD_NAME = (By.XPATH, ".//*[contains(@class, 'styles_single-card__title')]")
