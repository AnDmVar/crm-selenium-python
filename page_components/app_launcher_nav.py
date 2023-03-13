from selenium.webdriver.common.by import By
from base.base_page import BasePage


class AppLauncherNav(BasePage):

    # static locators
    APP_LAUNCHER_ICON = (By.XPATH, '//div[@class="slds-icon-waffle"]')

    # dynamic locator
    SALES_APP_MENU_ITEM_LOCATOR = '//a[@data-label="{}"]'

    def __init__(self, driver):
        super().__init__(driver)

    def goto_sales_app(self):
        self.wait_and_js_click(AppLauncherNav.APP_LAUNCHER_ICON, BasePage.TIMEOUT)
        self.wait_and_js_click((By.XPATH, AppLauncherNav.SALES_APP_MENU_ITEM_LOCATOR.format('Sales')), BasePage.TIMEOUT)

        from page_objects.Sales.sales_home_page import SalesHomePage
        return SalesHomePage(self.driver)
