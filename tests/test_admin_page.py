import allure
import pytest
from PageObjects.admin_page import AdminPage


@allure.step('Test that description actions is present')
@allure.feature('Admin page')
@allure.title('Test that description actions is present')
@pytest.mark.description_actions
def test_description_actions(browser, base_url):
    page_admin = AdminPage(browser, base_url + 'admin')
    page_admin.open()
    page_admin.should_be_description_actions()
