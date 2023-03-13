from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver

    # SELENIUM ACTIONS
    def click(self, by_locator):
        element = self.driver.find_element(*by_locator)
        element.click()

    @staticmethod
    def clear_and_enter_text(element, text):
        if text is None:
            return
        else:
            element.clear()
            element.send_keys(text)

    def enter_text(self, by_locator, text):
        element = self.driver.find_element(*by_locator)
        BasePage.clear_and_enter_text(element, text)

    def wait_and_enter_text(self, by_locator, text, timeout):
        element = self.wait_for_element_to_be_clickable(by_locator, timeout)
        BasePage.clear_and_enter_text(element, text)

    # JAVASCRIPT ACTIONS
    def js_click(self, by_locator):
        element = self.driver.find_element(*by_locator)
        self.driver.execute_script('arguments[0].click()', element)

    def wait_and_js_click(self, by_locator, timeout):
        element = self.wait_for_element_to_be_clickable(by_locator, timeout)
        self.driver.execute_script('arguments[0].click()', element)

    def scroll_into_view(self, by_locator, align_to_top=True):
        element = self.driver.find_element(*by_locator)
        self.driver.execute_script('arguments[0].scrollIntoView(arguments[1])', element, align_to_top)

    # EXPLICITLY WAIT
    def wait_for_element_to_be_clickable(self, by_locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator))

    def wait_for_visibility_of_element_located(self, by_locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
