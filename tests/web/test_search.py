from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage

def test_search_functionality(browser, base_url):
    login = LoginPage(browser)
    login.open(base_url)
    login.login('standard_user', 'secret_sauce')
    inv = InventoryPage(browser)
    items = inv.list_items()
    assert any('Sauce Labs Backpack' in item for item in items)
