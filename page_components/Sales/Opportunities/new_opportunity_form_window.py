from selenium.webdriver.common.by import By
from base.base_page import BasePage


class NewOpportunityFormWindow(BasePage):
    """This class represents the 'New Opportunity' form window."""

    # static locators
    FORM_PANEL = (By.XPATH, '//records-lwc-detail-panel')
    OPPORTUNITY_NAME_INPUT = (By.XPATH, '//input[@name="Name"]')
    ACCOUNT_NAME_INPUT = (By.XPATH, '//input[@placeholder="Search Accounts..."]')
    CLOSE_DATE_INPUT = (By.XPATH, '//input[@name="CloseDate"]')
    TYPE_LABEL = (By.XPATH, '//label[text()="Type"]')
    STAGE_COMBOBOX = (By.XPATH, '//label[text()="Stage"]')
    PRIMARY_CAMPAIGN_SOURCE_INPUT = (By.XPATH, '//label[text()="Primary Campaign Source"]')
    PROBABILITY_INPUT = (By.XPATH, '//input[@name="Probability"]')
    BUDGET_CONFIRMED_CHECKBOX = (By.XPATH, '//input[@name="Budget_Confirmed__c"]')
    AMOUNT_INPUT = (By.XPATH, '//input[@name="Amount"]')
    DISCOVERY_COMPLETED_CHECKBOX = (By.XPATH, '//input[@name="Discovery_Completed__c"]')
    ROI_ANALYSIS_COMPLETED_CHECKBOX = (By.XPATH, '//input[@name="ROI_Analysis_Completed__c"]')
    LOSS_REASON_COMBOBOX = (By.XPATH, '//label[text()="Loss Reason"]')
    NEXT_STEP_INPUT = (By.XPATH, '//input[@name="NextStep"]')
    LEAD_SOURCE_COMBOBOX = (By.XPATH, '//label[text()="Lead Source"]')
    DESCRIPTION_TEXTAREA = (By.XPATH, '//records-lwc-detail-panel//textarea')
    SAVE_BUTTON = (By.XPATH, '//records-lwc-detail-panel//button[@name="SaveEdit"]')

    # dynamic locators
    ACCOUNT_NAME_COMBOBOX_ITEM = '//lightning-base-combobox-formatted-text[@title="{}"]'
    STAGE_COMBOBOX_ITEM = '//span[@title="{}"]'

    def __init__(self, driver):
        super().__init__(driver)

    def create_opportunity(self, opportunity):
        """This method receives an opportunity entity as parameter and fills the form to creates an new opportunity."""

        # opportunity name
        self.wait_and_enter_text(NewOpportunityFormWindow.OPPORTUNITY_NAME_INPUT, opportunity.name, BasePage.TIMEOUT)

        # account name
        self.enter_text(NewOpportunityFormWindow.ACCOUNT_NAME_INPUT, opportunity.account_name)
        self.wait_and_js_click((By.XPATH, NewOpportunityFormWindow.ACCOUNT_NAME_COMBOBOX_ITEM.format(opportunity.account_name)), BasePage.TIMEOUT)

        # close date
        self.enter_text(NewOpportunityFormWindow.CLOSE_DATE_INPUT, opportunity.close_date)

        # type
        self.click(NewOpportunityFormWindow.TYPE_LABEL)
        self.wait_and_js_click((By.XPATH, NewOpportunityFormWindow.STAGE_COMBOBOX_ITEM.format(opportunity.type)), BasePage.TIMEOUT)

        # stage
        self.click(NewOpportunityFormWindow.STAGE_COMBOBOX)
        self.wait_and_js_click((By.XPATH, NewOpportunityFormWindow.STAGE_COMBOBOX_ITEM.format(opportunity.stage)), BasePage.TIMEOUT)

        # primary campaign source
        self.click(NewOpportunityFormWindow.PRIMARY_CAMPAIGN_SOURCE_INPUT)

        # probability
        self.enter_text(NewOpportunityFormWindow.PROBABILITY_INPUT, opportunity.probability)

        # budget confirmed
        self.click_checkbox(NewOpportunityFormWindow.BUDGET_CONFIRMED_CHECKBOX, opportunity.budget_confirmed)

        # amount
        self.enter_text(NewOpportunityFormWindow.AMOUNT_INPUT, opportunity.amount)

        # discovery completed
        self.click_checkbox(NewOpportunityFormWindow.DISCOVERY_COMPLETED_CHECKBOX, opportunity.discovery_completed)

        # roi analysis completed
        self.click_checkbox(NewOpportunityFormWindow.ROI_ANALYSIS_COMPLETED_CHECKBOX, opportunity.roi_analysis_completed)

        # scroll panel down
        self.scroll_into_view(NewOpportunityFormWindow.FORM_PANEL, False)

        # loss reason
        self.js_click(NewOpportunityFormWindow.LOSS_REASON_COMBOBOX)
        self.wait_and_js_click(self.get_combobox_item_locator('Loss Reason', opportunity.loss_reason), BasePage.TIMEOUT)

        # next step
        self.enter_text(NewOpportunityFormWindow.NEXT_STEP_INPUT, opportunity.nextstep)

        # lead source
        self.click(NewOpportunityFormWindow.LEAD_SOURCE_COMBOBOX)
        self.wait_and_js_click(self.get_combobox_item_locator('Lead Source', opportunity.lead_source), BasePage.TIMEOUT)

        # description
        self.enter_text(NewOpportunityFormWindow.DESCRIPTION_TEXTAREA, opportunity.description)

        # save form
        self.click(NewOpportunityFormWindow.SAVE_BUTTON)

        from page_objects.Sales.opportunity_view_page import OpportunityViewPage
        return OpportunityViewPage(self.driver)

    def click_checkbox(self, by_locator, to_be_checked):
        if to_be_checked:
            self.js_click(by_locator)

    def get_combobox_item_locator(self, label_text, combobox_item):
        label_element = self.wait_for_visibility_of_element_located((By.XPATH, f'//label[text()="{label_text}"]'), 0)
        label_id = label_element.get_attribute('for')
        combobox_item_locator = (By.XPATH, '//div[@id="{}"]//span[@title="{}"]'
                                 .format(label_id.replace('input', 'dropdown-element'), combobox_item))
        return combobox_item_locator
