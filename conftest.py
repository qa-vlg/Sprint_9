import os
import pytest
from urls import Urls
from data import UserData
from selenium.webdriver import Remote
from pages.login_page import LoginPage
from pages.recipe_page import RecipePage
from pages.sign_up_page import SignUpPage
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')

    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False
    })

    driver = Remote(
        command_executor=os.getenv("SELENOID_URL", "http://selenoid:4444/wd/hub"),
        options=options
    )
    driver.get(Urls.BASE_URL)    
    yield driver
    driver.quit()

@pytest.fixture
def sign_up_page(driver):
    sign_up_page = SignUpPage(driver)
    sign_up_page.navigate_to_sign_up_page()
    return sign_up_page

@pytest.fixture
def user_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    current_url, exit_button_present = login_page.user_login(UserData.email, UserData.password)
    return current_url, exit_button_present

@pytest.fixture
def recipe(driver, user_login):
    driver.get(Urls.RECIPES_PAGE_URL) 
    recipe_page = RecipePage(driver)
    recipe_page.navigate_to_recipe_tab()
    return recipe_page