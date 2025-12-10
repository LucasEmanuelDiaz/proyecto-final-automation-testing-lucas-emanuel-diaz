from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR = (By.CSS_SELECTOR, '[data-test="error"]')

    def open(self, base_url):
        super().open(base_url)

    def login(self, username, password):
        self.type(*self.USERNAME, text=username)
        self.type(*self.PASSWORD, text=password)
        self.click(*self.LOGIN_BUTTON)

    def get_error(self):
        try:
            return self.find(*self.ERROR).text
        except Exception:
            return None
