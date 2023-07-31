import os

from driver_utils.driver_inst import WebDriver
from tests.config import Config
from utils.singleton import Singleton


class Driver(metaclass=Singleton):
    """
    Get driver and driver`s methods
    """
    driver = None

    def __init__(self):
        self.driver = WebDriver().get_driver_instance()

    def get_driver(self):
        return self.driver

    def get_screenshot(self):
        self.driver.save_screenshot(
            f'{Config.PATH_SAVE_SCREENSHOTS}/screenshot.png'
        )

    @staticmethod
    def driver_quit(driver):
        Singleton._instances = {}
        driver.quit()

    @staticmethod
    def press_home_btn():
        os.system(f"adb shell input keyevent {Config.PRESS_HOME_BTN_KEY_EVENT_CODE}")
