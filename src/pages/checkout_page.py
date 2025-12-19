from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE = (By.ID, 'continue')
    FINISH = (By.ID, 'finish')

    def fill_info_and_continue(self, first, last, postal):
        self.type(*self.FIRST_NAME, text=first)
        self.type(*self.LAST_NAME, text=last)
        self.type(*self.POSTAL_CODE, text=postal)
        self.click(*self.CONTINUE)

    def finish(self):
        self.wait.until(EC.url_contains("checkout-step-two"))

        finish_btn = self.wait.until(
            EC.element_to_be_clickable(self.FINISH)
        )
        finish_btn.click()
