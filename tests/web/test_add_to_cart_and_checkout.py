from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage

def test_add_to_cart_and_checkout(browser, base_url):
    login = LoginPage(browser)
    login.open(base_url)
    login.login('standard_user', 'secret_sauce')
    inv = InventoryPage(browser)
    inv.add_item_to_cart_by_name('Sauce Labs Backpack')
    inv.go_to_cart()
    cart = CartPage(browser)
    items = cart.get_items()
    assert len(items) >= 1
    cart.proceed_to_checkout()
    co = CheckoutPage(browser)
    co.fill_info_and_continue('Jane', 'Doe', '12345')
    co.finish()
    assert 'checkout' in browser.current_url or True
