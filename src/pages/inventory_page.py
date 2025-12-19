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

    def add_item_to_cart_by_name(self, name):
        WebDriverWait(self.driver, 15).until(
        EC.url_contains("inventory")
        )
        xpath = f"//div[@class='inventory_item']//div[@class='inventory_item_name' and text()='{name}']/ancestor::div[@class='inventory_item']//button"
        self.click(By.XPATH, xpath)

    def go_to_cart(self):
        self.click(*self.CART_LINK)
