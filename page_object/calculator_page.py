import os

from appium.webdriver.common.mobileby import MobileBy

from page_object.element.button import Button
from page_object.element.lable import Label


class CalculatorPage:
    """
    Operations:
    - addition,
    - get a result.
    """

    DIGIT = 'com.google.android.calculator:id/digit_{}'
    PLUS_BTN = 'com.google.android.calculator:id/op_add'
    EQUAL_BTN = 'com.google.android.calculator:id/eq'
    SCREEN_FORMULA = 'com.google.android.calculator:id/result_final'
    MINUS_BTN = 'com.google.android.calculator:id/op_sub'
    CLEAR_BTN = 'com.google.android.calculator:id/clr'

    def add_two_positive_nums(self, num_1, num_2):
        """
        Add numbers 0...9.
        """
        Button(MobileBy.ID, self.CLEAR_BTN, "Clear").tap()
        Button(MobileBy.ID, self.DIGIT.format(num_1), f"{num_1}").tap()
        Button(MobileBy.ID, self.PLUS_BTN, "+").tap()
        Button(MobileBy.ID, self.DIGIT.format(num_2), f"{num_2}").tap()
        Button(MobileBy.ID, self.EQUAL_BTN, "=").tap()

    def get_result(self):
        return Label(MobileBy.ID, self.SCREEN_FORMULA, "Get result").get_label_text()

    @staticmethod
    def addition_positive_num_tap_with_keyevent(num_1, num_2):
        """
        Add numbers 0...9.
        """
        os.system("adb shell input keyevent KEYCODE_CLEAR")
        os.system(f"adb shell input keyevent KEYCODE_{num_1}")
        os.system("adb shell input keyevent KEYCODE_PLUS")
        os.system(f"adb shell input keyevent KEYCODE_{num_2}")
        os.system("adb shell input keyevent KEYCODE_EQUALS")
