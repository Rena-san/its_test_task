import allure
import pytest

from driver_utils.driver import Driver
# from time import sleep
from page_object.android_page import AndroidPage


@allure.feature("send_result")
@pytest.mark.usefixtures("set_up")
class TestCase:
    def test_get_screenshot(self):
        home_page = AndroidPage()
        Driver().press_home_btn()

        home_page.send_text_to_google_search(
            'passed: 2 , failed: 2 , total: 4'
        )
        Driver().get_screenshot()
        Driver().press_home_btn()
