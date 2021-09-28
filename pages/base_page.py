from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = "http://localhost:8000/"
        self.image = None

    def open_main_page(self):
        self.driver.get(self.base_page)

    def find_element(self, locator: tuple, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f'Can not find element by locator {locator}'
        )
