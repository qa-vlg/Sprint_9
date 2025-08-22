from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def get_page_element_text(self, locator):
        text = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).text
        return text
    
    def wait_for_element_to_be_ready(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        return element
    
    def wait_for_element_to_be_present(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    def get_page_url(self):
        return self.driver.current_url
    
    def get_all_elements(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        return elements
        
    def click_on_element_with_js(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def click_on_element(self, locator):
         element = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))
         element.click()

    def click_on_a_list_item(self, list_item):
        list_item.click()

    def enter_text(self, locator, text):
         element = self.find_element_with_wait(locator)
         element.send_keys(text)
    
    def element_not_present(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True
    
    def element_is_present(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True
    
    def dismiss_a_modal(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def upload_photo(self, locator, file):
        uploader = self.driver.find_element(*locator)
        uploader.send_keys(file)

    def scroll_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_for_element_to_disapear(self, locator):
        try:
             WebDriverWait(self.driver, 20).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException('might want to increase wait time or revisit the logic')