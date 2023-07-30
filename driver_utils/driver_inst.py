from appium import webdriver


class WebDriver:

    @staticmethod
    def get_driver_instance(host, capabilities):
        """
        Returns an instance of webdriver
        """
        driver = webdriver.Remote(host, desired_capabilities=capabilities)
        return driver

