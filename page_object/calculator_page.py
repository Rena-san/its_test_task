import os

from appium.webdriver.common.mobileby import MobileBy

from page_object.element.button import Button
from page_object.element.lable import Label
from tests.calc_btn_coord_parser import calc_btn_coord


class CalculatorPage:
    """
    Methods (actions) of calculator:
    + plus,
    — minus,
    clear screen
    """

    DIGIT = 'com.google.android.calculator:id/digit_{}'
    PLUS_BTN = 'com.google.android.calculator:id/op_add'
    EQUAL_BTN = 'com.google.android.calculator:id/eq'
    SCREEN_FORMULA = 'com.google.android.calculator:id/result_final'
    MINUS_BTN = 'com.google.android.calculator:id/op_sub'
    PAGE_TAG = 'com.google.android.calculator:id/clr'

    def add_two_positive_nums(self, num_1, num_2):
        """
        Add numbers 0...9.
        """
        Button(MobileBy.ID, self.DIGIT.format(num_1), f"{num_1}").tap()
        Button(MobileBy.ID, self.PLUS_BTN, "+").tap()
        Button(MobileBy.ID, self.DIGIT.format(num_2), f"{num_2}").tap()
        Button(MobileBy.ID, self.EQUAL_BTN, "=").tap()

    def subtract_two_positive_nums(self, num_1, num_2):
        Button(MobileBy.ID, self.DIGITS.format(id=num_1), f"{num_1}").tap()
        Button(MobileBy.ID, self.MINUS_BTN, "-").tap()
        Button(MobileBy.ID, self.DIGITS.format(id=num_2), f"{num_2}").tap()
        Button(MobileBy.ID, self.EQUAL_BTN, "=").tap()

    def get_result(self):
        return Label(MobileBy.ID, self.SCREEN_FORMULA, "Get result").get_label_text()

    # def clear_screen(self):
    #     Button(MobileBy.ID, self.CLEAR_BTN, "Clear screen")

    @staticmethod
    def addition_positive_num_tap_with_coordinates(num_1, num_2):
        """
        Add numbers 0...9.
        """
        x_1, y_1 = calc_btn_coord()[f"{num_1}"]
        os.system(f"adb shell input tap {x_1} {y_1}")
        x_pl, y_pl = calc_btn_coord()["+"]
        os.system(f"adb shell input tap {x_pl} {y_pl}")
        x_2, y_2 = calc_btn_coord()[f"{num_2}"]
        os.system(f"adb shell input tap {x_2} {y_2}")
        x_eq, y_eq = calc_btn_coord()["="]
        os.system(f"adb shell input tap {x_eq} {y_eq}")
