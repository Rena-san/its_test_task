from appium import webdriver
from tests.config import Config


class WebDriver:

    @staticmethod
    def get_driver_instance():
        """
        Returns an instance of webdriver
        """
        driver = webdriver.Remote(
            Config.HOST,
            desired_capabilities=Config.get_capabilities()
        )
        driver.implicitly_wait(Config.WAITS)
        return driver
