import os
from datetime import datetime

class ScreenshotUtil:
    @staticmethod
    def save(driver, test_name: str):
        folder = os.path.join(os.getcwd(), 'reports', 'screenshots')
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{test_name}_{timestamp}.png"
        path = os.path.join(folder, filename)
        driver.save_screenshot(path)
        return path
