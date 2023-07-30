from time import sleep

import pytest

from driver_utils.driver import Driver
from page_object.android_page import AndroidPage
from page_object.calculator_page import CalculatorPage
from tests.config_parser import config


@pytest.mark.parametrize("nums", ([1, 2], [3, 4]))
@pytest.mark.usefixtures("set_up")
class TestCase:
    def test_addition(self, nums):
        Driver().press_home_btn()
        home_page = AndroidPage()
        home_page.press_calc_app()
        calculator = CalculatorPage()
        sleep(1)
        calculator.add_two_positive_nums(*nums)
        s = calculator.get_result()
        assert s == f'{sum(nums)}', "Wrong result"
        Driver().press_home_btn()



