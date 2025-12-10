import pytest
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.utils.data_helpers import read_users_csv, read_users_json

@pytest.mark.web
@pytest.mark.parametrize('user', read_users_csv())
def test_login_param_csv(browser, base_url, user):
    login = LoginPage(browser)
    login.open(base_url)
    login.login(user['username'], user['password'])
    inv = InventoryPage(browser)
    if user['expected'] == 'success':
        assert 'Products' in inv.get_title()
    else:
        assert login.get_error() is not None

@pytest.mark.web
@pytest.mark.parametrize('user', read_users_json())
def test_login_param_json(browser, base_url, user):
    login = LoginPage(browser)
    login.open(base_url)
    login.login(user['username'], user['password'])
    if user['expected'] == 'success':
        inv = InventoryPage(browser)
        assert 'Products' in inv.get_title()
    else:
        assert login.get_error() is not None
