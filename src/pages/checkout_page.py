from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

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
        self.wait.until(EC.url_contains("checkout-step-one"))

        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).clear()
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)

        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).clear()
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last)

        self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE)).clear()
        self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE)).send_keys(zip_code)

        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()

        try:
            self.wait.until(EC.presence_of_element_located(self.FINISH))
        except TimeoutException:
            error = self.driver.find_elements(By.CLASS_NAME, "error-message-container")
            if error:
                raise AssertionError(f"Checkout bloqueado por SauceDemo: {error[0].text}")
            else:
                raise AssertionError("Checkout no avanzó a step two (sin mensaje visible)")

    def finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH)).click()


