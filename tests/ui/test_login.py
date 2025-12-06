from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_success(driver):
    login = LoginPage(driver)
    login.go()
    login.login('standard_user', 'secret_sauce')
    inv = InventoryPage(driver)
    assert 'Products' in inv.get_title()
