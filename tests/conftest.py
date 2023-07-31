import pytest

from driver_utils.driver import Driver


@pytest.fixture()
def set_up():
    driver = Driver().get_driver()

    yield driver

    Driver().driver_quit(driver)


def pytest_addoption(parser):
    parser.addoption(
        '--deviceName',
        action="store",
        help="Real Device or Android Emulator"
    )
