import time

from base.base_page import BasePage
from selenium.webdriver.common.by import By


class SalesNavigationBar(BasePage):
    # dynamic locators
    NAV_MENU_ITEM_DROPDOWN = '//span[text()="{}"]/parent::a/following-sibling::one-app-nav-bar-item-dropdown//one-app' \
                             '-nav-bar-menu-button/a'
    # static locators
    NEW_OPPORTUNITY_SUB_MENU_ITEM = (By.XPATH, '//span[@one-appnavbarmenuitem_appnavbarmenuitem'
                                               ' and text()="New Opportunity"]')

    def __init__(self, driver):
        super().__init__(driver)

    # user actions
    def goto_new_opportunity_window(self):
        time.sleep(5)
        self.click_nav_menu_dropdown('Opportunities')\
            .wait_and_js_click(SalesNavigationBar.NEW_OPPORTUNITY_SUB_MENU_ITEM, BasePage.TIMEOUT)

        from page_components.Sales.Opportunities.new_opportunity_form_window import NewOpportunityFormWindow
        return NewOpportunityFormWindow(self.driver)

    # helper methods
    def click_nav_menu_dropdown(self, nav_menu_item_text):
        dropdown_locator = (By.XPATH, SalesNavigationBar.NAV_MENU_ITEM_DROPDOWN.format(nav_menu_item_text))
        self.wait_and_js_click(dropdown_locator, BasePage.TIMEOUT)
        return self
