from pages.login_page import LoginPage

def test_login_invalid(driver):
    login = LoginPage(driver)
    login.go()
    login.login('invalid_user', 'badpass')
    assert 'Epic sadface' in login.get_error()
