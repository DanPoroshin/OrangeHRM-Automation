import allure
from base.base_test import BaseTest
import pytest

@allure.feature("Profile")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_name("Alexander")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("profile_name_changed")