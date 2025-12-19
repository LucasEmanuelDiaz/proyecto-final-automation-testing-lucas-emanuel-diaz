from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, 'title')
    ITEM_NAMES = (By.CLASS_NAME, 'inventory_item_name')
    CART_LINK = (By.ID, 'shopping_cart_container')

    def get_title(self):
        return self.find(*self.TITLE).text

    def list_items(self):
        elems = self.find_all(*self.ITEM_NAMES)
        return [e.text for e in elems]

    def add_item_to_cart_by_name(self, product_name):
        self.wait.until(EC.url_contains("inventory"))

        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_btn.click()

        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "shopping_cart_badge"), "1"
            )
        )

    def go_to_cart(self):
        self.click(*self.CART_LINK)
