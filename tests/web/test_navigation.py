from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage

def test_navigation_after_login(browser, base_url):
    login = LoginPage(browser)
    login.open(base_url)
    login.login('standard_user', 'secret_sauce')
    inv = InventoryPage(browser)
    title = inv.get_title()
    assert 'Products' in title
    items = inv.list_items()
    assert len(items) > 0
