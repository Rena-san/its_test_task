import pytest

from driver_utils.driver import Driver


@pytest.fixture(scope="function", autouse=True)
def set_up():
    driver = Driver().get_driver()

    yield driver


    Driver().driver_quit(driver)


def pytest_addoption(parser):
    parser.addoption(
        '--deviceName',
        action="store",
        help="The kind of mobile device or emulator to use: Samsung Tab, Android Emulator"
    )




@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--deviceName")


    #prints test run statistic in terminal

# def pytest_sessionfinish(session, exitstatus):
#     reporter = session.config.pluginmanager.get_plugin('terminalreporter')
#     passed = len(reporter.stats['passed'])
#     failed = len(reporter.stats['failed'])
#     total = passed + failed
#     print(f'passed:{passed}, failed: {failed}, total: {total}')
