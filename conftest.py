import pytest
from utils.driver_factory import DriverFactory
from utils.data_loader import DataLoader
from utils.screenshot_util import ScreenshotUtil
import os

@pytest.fixture(scope="session")
def config():
    return {
        "base_url": "https://www.saucedemo.com",
        "headless": False  # pon True para headless
    }

@pytest.fixture(scope="function")
def driver(request, config):
    driver = DriverFactory.create_driver(headless=config["headless"])
    yield driver

    # --- hook-safe check para saber si falló la fase 'call' del test ---
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        # guardamos screenshot con nombre descriptivo
        path = ScreenshotUtil.save(driver, request.node.name)
        # si usás pytest-html, podés adjuntarla desde el hook (ver README)
        print(f"[INFO] Screenshot guardada en: {path}")
    driver.quit()

def pytest_runtest_makereport(item, call):
    """
    Hook que crea atributos rep_setup/rep_call/rep_teardown en el node.
    Así fixtures pueden inspeccionar el resultado de la ejecución.
    """
    setattr(item, "rep_" + call.when, call)
