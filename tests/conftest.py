import pytest
from filelock import FileLock
import json
from utils.driver_factory import DriverFactory
from utils import config_util
from page_objects.login_page import LoginPage
from selenium.common.exceptions import InvalidSessionIdException


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', choices=['chrome', 'edge', 'firefox'], default='edge', type=str)
    parser.addoption('--headless', action='store', choices=['no', 'yes'], default='no', type=str)
    parser.addoption('--environment', action='store', choices=['local', 'remote'], default='local', type=str)


def configure_driver(request):
    # make the DriverFactory object serializable to share it among workers
    # by converting its variables into a dictionary of key-value pairs
    return DriverFactory(request.config.getoption('--browser'),
                         request.config.getoption('--headless'),
                         request.config.getoption('--environment')).__dict__


@pytest.fixture(scope='session')
def session_data(request, tmp_path_factory, worker_id):
    if worker_id == 'master':
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return configure_driver(request)

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / 'data.json'
    with FileLock(str(fn) + '.lock'):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = configure_driver(request)
            fn.write_text(json.dumps(data))
    return data


@pytest.fixture(scope='function', autouse=True)
def open_close_app(request, session_data):
    section = 'test'

    driver = DriverFactory.get_new_driver(session_data['driver_options'], session_data['driver_builder'])
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.set_page_load_timeout(config_util.get_value(section, 'page_load_timeout'))

    driver.get(config_util.get_value(section, 'app_url'))
    LoginPage(driver).login(config_util.get_value(section, 'username'), config_util.get_value(section, 'password'))

    request.cls.driver = driver
    yield
    try:
        driver.close()
        driver.quit()
    except InvalidSessionIdException:
        # this exception usually occurs with geckodriver because the driver.close() method
        # also quits the session if it's called on the last window
        pass
