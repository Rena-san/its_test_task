from appium.webdriver.common.mobileby import MobileBy

from page_object.element.button import Button
from page_object.element.input import Input


class HomePage:
    """
    Methods (actions) of home screen.
    """
    CALC_APP = '//android.widget.TextView[@content-desc="Calculator"]'
    SEARCH_WIDJET = '//*[contains(@content-desc,"search") or \
                        contains(@content-desc,"Search")]'

    GOOGLE_SEARCH = '//*[contains(@class, "android.widget.EditText")]'

    def send_text_to_google_search(self, text):
        Button(MobileBy.XPATH, self.SEARCH_WIDJET, "search_bar").tap()
        Input(MobileBy.XPATH, self.GOOGLE_SEARCH, "google").send_text(text)

    def press_calc_app(self):
        Button(MobileBy.XPATH, self.CALC_APP, "calc_app").tap()
