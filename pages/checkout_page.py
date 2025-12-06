from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRSTNAME = (By.ID, 'first-name')
    LASTNAME = (By.ID, 'last-name')
    ZIP = (By.ID, 'postal-code')
    CONTINUE = (By.ID, 'continue')
    FINISH = (By.ID, 'finish')

    def fill_info(self, first, last, zipc):
        self.type(self.FIRSTNAME, first)
        self.type(self.LASTNAME, last)
        self.type(self.ZIP, zipc)
        self.click(self.CONTINUE)

    def finish(self):
        self.click(self.FINISH)
