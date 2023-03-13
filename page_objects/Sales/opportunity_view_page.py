from base.base_page import BasePage
from selenium.webdriver.common.by import By


class OpportunityViewPage(BasePage):

    # static locators
    OPPORTUNITY_NAME_TITLE = (By.XPATH, '//h1//lightning-formatted-text')

    def __init__(self, driver):
        super().__init__(driver)

    def get_opportunity_name(self):
        opportunity_element = self.wait_for_visibility_of_element_located(OpportunityViewPage.OPPORTUNITY_NAME_TITLE, BasePage.TIMEOUT)
        return opportunity_element.text
