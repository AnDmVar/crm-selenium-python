#
# Do not remove these imported packages, they are required for exec and eval functions!
#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from msedge.selenium_tools import Edge
from msedge.selenium_tools import EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory(object):

    def __init__(self, browser, headless, environment):
        def set_options(options):
            options += '; options.add_argument("--disable-notifications")'
            if headless == 'yes':
                options += '; options.add_argument("--headless")'
                options += '; options.add_argument("--disable-gpu")'
            return options

        def set_environment(driver_class, driver_installation):
            if environment == 'local':
                return driver_class + '(**{"executable_path": ' + repr(eval(driver_installation)) + '}, options=options)'
            else:
                from utils import config_util
                return 'webdriver.Remote(**{"command_executor": "' + config_util.get_value('test', 'hub_url') + '"}, options=options)'

        if browser == 'chrome':
            self.driver_options = set_options('options = ChromeOptions()')
            self.driver_builder = set_environment('webdriver.Chrome', 'ChromeDriverManager().install()')
        elif browser == 'edge':
            self.driver_options = set_options('options = EdgeOptions(); options.use_chromium = True')
            self.driver_builder = set_environment('Edge', 'EdgeChromiumDriverManager().install()')
        else:
            self.driver_options = set_options('options = FirefoxOptions()')
            self.driver_builder = set_environment('webdriver.Firefox', 'GeckoDriverManager().install()')

    @staticmethod
    def get_new_driver(driver_options, driver_builder):
        exec(driver_options)
        return eval(driver_builder)
