from base.base_page import BasePage


class SalesHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        from page_components.Sales.sales_navigation_bar import SalesNavigationBar
        self.sales_navigation_bar = SalesNavigationBar(driver)
