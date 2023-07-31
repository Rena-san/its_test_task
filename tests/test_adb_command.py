from time import sleep

import allure
import pytest

from driver_utils.driver import Driver
from page_object.calculator_page import CalculatorPage
from page_object.home_page import HomePage
from tests.calc_btn_coord_parser import calc_btn_coord


@allure.feature("addition with coord")
@pytest.mark.parametrize("nums", ([1, 2], [3, 4]))
@pytest.mark.usefixtures("set_up")
class TestCase:
    """
    Negative tests.
    Add two positive num from 0 till 9.
    """
    def test_addition_tap_with_coord(self, nums):
        home_page = HomePage()
        Driver().press_home_btn()
        home_page.press_calc_app()
        calculator = CalculatorPage()
        sleep(1)
        calculator.addition_positivе_num_tap_with_coordinates(*nums)
        s = calculator.get_result()
        assert s == '5', "Wrong result"
