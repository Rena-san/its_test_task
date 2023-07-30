import os

from driver_utils.driver_inst import WebDriver
from tests.config import Config
from utils.singleton import Singleton

adbpath = r"d:\Android\sdk\platform-tools"
adbfile = 'adb.exe'
adb = os.path.join(adbpath, adbfile)


class Driver(metaclass=Singleton):
    """
    Get driver and driver`s methods
    """
    driver = None

    def __init__(self):
        self.driver = WebDriver().get_driver_instance(
            Config.HOST,
            Config.get_capabilities()
        )

    def get_driver(self):
        return self.driver

    @staticmethod
    def driver_quit(driver):
        Singleton._instances = {}
        driver.quit()

    def get_screenshot(self):
        self.driver.save_screenshot(
            'D:\\\\ITS_PROJECT_TEST_TASK\\\\appium\\\\test_task\\\\its_test_task\\\\scr.png')

    @staticmethod
    def press_home_btn():
        os.system(f"adb shell input keyevent 3")
