from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    ITEMS = (By.CLASS_NAME, 'cart_item')

    def proceed_to_checkout(self):
        self.click(*self.CHECKOUT_BUTTON)

    def get_items(self):
        return self.find_all(*self.ITEMS)
