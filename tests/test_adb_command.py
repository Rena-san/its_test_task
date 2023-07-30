from time import sleep

import allure
import pytest

from driver_utils.driver import Driver
from page_object.android_page import AndroidPage
from page_object.calculator_page import CalculatorPage
from tests.config_parser import config


@allure.feature("addition with coord")
@pytest.mark.parametrize("nums", ([1, 2], [3, 4]))
@pytest.mark.usefixtures("set_up")
class TestCase:
    def test_addition_tap_with_coord(self, nums):
        home_page = AndroidPage()
        Driver().press_home_btn()
        home_page.press_calc_app()
        calculator = CalculatorPage()
        sleep(1)
        calculator.addition_positivе_num_tap_with_coordinates(*nums)
        s = calculator.get_result()
        assert s == '5', "Wrong result"
