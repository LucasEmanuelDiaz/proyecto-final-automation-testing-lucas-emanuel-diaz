from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    ITEMS = (By.CLASS_NAME, 'cart_item')

    def proceed_to_checkout(self):
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items) > 0, "El carrito está vacío"

        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()


    def get_items(self):
        return self.find_all(*self.ITEMS)
