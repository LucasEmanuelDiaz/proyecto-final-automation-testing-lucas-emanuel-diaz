from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def fill_info_and_continue(self, first, last, zip_code):
    # Confirmar step one
        self.wait.until(EC.url_contains("checkout-step-one"))

        first_name = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME))
        last_name = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME))
        postal = self.wait.until(EC.element_to_be_clickable(self.POSTAL_CODE))

        first_name.clear()
        first_name.send_keys(first)

        last_name.clear()
        last_name.send_keys(last)

        postal.clear()
        postal.send_keys(zip_code)

        # 🔥 SUBMIT REAL DEL FORMULARIO
        postal.send_keys(Keys.ENTER)

        # ✅ ESPERAR que la página siguiente esté lista
        self.wait.until(EC.presence_of_element_located(self.FINISH))



    def finish(self):
        finish_btn = self.wait.until(
        EC.element_to_be_clickable(self.FINISH)
    )
        finish_btn.click()

