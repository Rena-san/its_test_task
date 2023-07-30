from driver_utils.driver import Driver


class Element:
    """
    Base methods of elements.
    """
    def __init__(self, search_condition, locator, name):
        self.search_condition = search_condition
        self.name = name
        self.locator = locator

    def find_element(self):
        element = Driver().get_driver().find_element(self.search_condition, self.locator)
        return element

    def tap(self):
        self.find_element().click()

