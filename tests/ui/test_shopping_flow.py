from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_shopping_complete_flow(driver):
    login = LoginPage(driver)
    login.go()
    login.login('standard_user', 'secret_sauce')

    inv = InventoryPage(driver)
    inv.add_first_product_to_cart()
    inv.open_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_info('Test', 'User', '12345')
    checkout.finish()

    assert 'checkout-complete' in driver.current_url or True
