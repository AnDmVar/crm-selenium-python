from base.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'Login')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.enter_text(LoginPage.USERNAME_FIELD, username)
        self.enter_text(LoginPage.PASSWORD_FIELD, password)
        self.click(LoginPage.LOGIN_BUTTON)
        from page_objects.Sales.sales_home_page import SalesHomePage
        return SalesHomePage(self.driver)
