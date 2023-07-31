import pytest

from driver_utils.driver import Driver
from page_object.calculator_page import CalculatorPage
from page_object.home_page import HomePage


@pytest.mark.parametrize("nums", ([1, 2], [3, 4]))
@pytest.mark.usefixtures("set_up")
class TestCase:
    """
       Positive tests.
       Add two positive num from 0 till 9.
    """
    def test_addition(self, nums):
        Driver().press_home_btn()
        home_page = HomePage()
        home_page.press_calc_app()
        calculator = CalculatorPage()
        calculator.add_two_positive_nums(*nums)
        s = calculator.get_result()
        assert s == f'{sum(nums)}', "Wrong result"
        Driver().press_home_btn()



