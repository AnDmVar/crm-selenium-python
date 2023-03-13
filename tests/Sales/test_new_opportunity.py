import allure
from allure import severity_level
import pytest
from page_components.app_launcher_nav import AppLauncherNav
from entities.opportunity import Opportunity
from databases.mysql import db_connector


def valid_opportunity_records():
    db_connection = db_connector.create_connection()
    db_connector.use(db_connection)

    data = []
    for record in db_connector.read_query(db_connection, 'SELECT * FROM opportunity', dictionary=True):
        data.append((Opportunity(**record)))

    db_connection.close()
    return data


@allure.tag('Sales', 'Smoke', 'Regression')
class TestNewOpportunity(object):

    @allure.description(test_description='Test the "New Opportunity" functionality with valid opportunity form data.')
    @allure.severity(severity_level=severity_level.CRITICAL)
    @pytest.mark.parametrize('opportunity', valid_opportunity_records())
    def test_valid_new_opportunity(self, opportunity: Opportunity):
        assert(AppLauncherNav(self.driver)
               .goto_sales_app()
               .sales_navigation_bar
               .goto_new_opportunity_window()
               .create_opportunity(opportunity)
               .get_opportunity_name() == opportunity.name)
