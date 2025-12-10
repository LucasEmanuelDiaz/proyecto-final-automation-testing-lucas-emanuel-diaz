import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from src.utils.logger import get_logger

LOGGER = get_logger()

@pytest.fixture(scope='session')
def base_url():
    return 'https://www.saucedemo.com'

@pytest.fixture(scope='function')
def browser(request):
    options = Options()
    # comment out headless if you want to see the browser
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.set_window_size(1280, 1024)
    LOGGER.info('Browser started')

    yield driver

    LOGGER.info('Quitting browser')
    driver.quit()

# Hook to take screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get('browser')
        if driver is not None:
            screenshots_dir = os.path.join(os.getcwd(), 'screenshots')
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            test_name = item.name
            filename = f"{test_name}_{timestamp}.png"
            path = os.path.join(screenshots_dir, filename)
            try:
                driver.save_screenshot(path)
                LOGGER.error(f"Screenshot saved to {path}")
                # attach to html report (pytest-html)
                try:
                    from pytest_html import extras
                    if hasattr(rep, 'extra'):
                        rep.extra.append(extras.image(path))
                except Exception:
                    pass
            except Exception as e:
                LOGGER.exception('Failed to take screenshot: %s', e)
