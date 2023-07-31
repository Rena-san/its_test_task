import os

from utils.get_args import get_args


class Config:
    """
    Configurations of webdriver for emulator and real device.
    """
    HOST = 'http://localhost:4723/wd/hub'
    CAPABILITIES_EMULATOR = {
        "platformName": "Android",
        "automationName": "UIAutomator2",
        "platformVersion": "11.0",
        "deviceName": "Android Emulator"
    }

    CAPABILITIES_DEVICE = {
        "deviceName": "Samsung Tab",
        "platformName": "Android",
        "platformVersion": "12.0"
    }

    PRESS_HOME_BTN_KEY_EVENT_CODE = 3
    PATH_SAVE_SCREENSHOTS = os.path.dirname(os.path.realpath(__file__))
    WAITS = 3

    @staticmethod
    def get_capabilities():
        deviceName = get_args()
        if deviceName['deviceName'] is None:
            return Config.CAPABILITIES_EMULATOR
        if deviceName['deviceName'] == 'emulator':
            return Config.CAPABILITIES_EMULATOR
        if deviceName['deviceName'] == 'real':
            return Config.CAPABILITIES_DEVICE
        else:
            raise Exception(f'{deviceName} is not a support device')
