import allure
import pytest

from driver_utils.driver import Driver
from page_object.home_page import HomePage


@allure.feature("send_result")
@pytest.mark.usefixtures("set_up")
class TestCase:
    """
    Get screenshot
    """
    def test_get_screenshot(self):
        home_page = HomePage()
        Driver().press_home_btn()

        home_page.send_text_to_google_search(
            'passed: 2 , failed: 2 , total: 4'
        )
        Driver().get_screenshot()
        Driver().press_home_btn()
