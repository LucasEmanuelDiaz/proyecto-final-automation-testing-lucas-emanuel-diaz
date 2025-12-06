from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, 'title')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.inventory_item button')
    CART_LINK = (By.ID, 'shopping_cart_container')

    def add_first_product_to_cart(self):
        self.find(self.ADD_TO_CART_BTN).click()

    def open_cart(self):
        self.click(self.CART_LINK)

    def get_title(self):
        return self.find(self.TITLE).text
