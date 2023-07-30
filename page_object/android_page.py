import os
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from driver_utils.driver import Driver
from page_object.element.button import Button
from page_object.element.input import Input
# from subprocess import Popen, PIPE
from tests.config_parser import config


class AndroidPage:
    """
    Method`s (actions) of home screen.
    """
    PAGE_TAG = '//android.widget.TextView[@content-desc="Phone"]'
    GOOGLE_SEARCH = 'com.android.quicksearchbox:id/search_src_text'
    SEARCH_WIDJET = 'com.android.quicksearchbox:id/search_widget_text'
    CALC_APP = '//android.widget.TextView[@content-desc="Calculator"]'

    def send_text_to_google_search(self, text):
        Button(MobileBy.ID, self.SEARCH_WIDJET, "search_bar").tap()
        sleep(3)

        Input(MobileBy.ID, self.GOOGLE_SEARCH, "google").send_text(text)

    def press_calc_app(self):
        Button(MobileBy.XPATH, self.CALC_APP, "calc_app").tap()