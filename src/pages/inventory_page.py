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

        product_ids = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bike Light": "add-to-cart-sauce-labs-bike-light"
        }

        product_id = product_ids.get(product_name)
        if not product_id:
            raise ValueError(f"Producto no reconocido: {product_name}")

        
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, product_id))
        )
        add_btn.click()

    def go_to_cart(self):
        self.click(*self.CART_LINK)
