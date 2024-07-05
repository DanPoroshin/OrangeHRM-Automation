import allure
from base.base_test import BaseTest
import pytest

@allure.feature("Profile")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile first name")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_name("Alexander")
        self.personal_page.save_personal_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("profile_name_changed")


    @allure.title("Change profile middle name")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    def test_change_profile_middle_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_middle_name("Petrov")
        self.personal_page.save_personal_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("profile_middle_name_changed")

    @allure.title("Change profile last name")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    def test_change_profile_last_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_last_name("Ivanov")
        self.personal_page.save_personal_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("profile_last_name_changed")


    @allure.title("Change profile employee id")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    def test_change_employee_id(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_employee_id("5768")
        self.personal_page.save_personal_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("profile_employee_id_changed")


    @allure.title("Change profile license id")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    def test_change_license_id(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_license_id("123456")
        self.personal_page.save_personal_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("profile_license_id_changed")


    @allure.title("Change profile license expiry date")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    def test_change_license_expiry_date(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_license_expiry_date_by_input("2025-01-01")
        self.personal_page.save_personal_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("profile_license_expiry_date_changed")


    @allure.title("Change profile nationality")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.positive
    def test_change_nationality(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_nationality("Russian")
        self.personal_page.save_personal_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("profile_nationality_changed")


    @allure.title("Change profile marital status")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.positive
    def test_change_marital_status(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_marital_status("Married")
        self.personal_page.save_personal_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("profile_marital_status_changed")

    @allure.title("Change profile date of birth")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.positive
    def test_change_profile_date_of_birth(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_date_of_birth_by_input("1990-01-01")
        self.personal_page.save_personal_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("profile_date_of_birth_changed")
    
    @allure.title("Change profile gender")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.positive
    def test_change_profile_gender(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_gender("Male")
        self.personal_page.save_personal_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("profile_gender_changed")