import allure
import time
from base.base_page import BasePage
from config.links import Links
from fields.personal_page_fields import PersonalPageFields as Fields
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE
    def change_name(self, name):
        with allure.step(f"Change name to {name}"):
            time.sleep(1)
            first_name_field = self.wait.until(EC.element_to_be_clickable(Fields.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.CONTROL + "a")
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(name)

    def change_middle_name(self, middle_name):
        with allure.step(f"Change middle name to {middle_name}"):
            time.sleep(1)
            middle_name_field = self.wait.until(EC.element_to_be_clickable(Fields.MIDDLE_NAME_FIELD))
            middle_name_field.send_keys(Keys.CONTROL + "a")
            middle_name_field.send_keys(Keys.BACKSPACE)
            middle_name_field.send_keys(middle_name)
    
    def change_last_name(self, last_name):
        with allure.step(f"Change last name to {last_name}"):
            time.sleep(1)
            last_name_field = self.wait.until(EC.element_to_be_clickable(Fields.LAST_NAME_FIELD))
            last_name_field.send_keys(Keys.CONTROL + "a")
            last_name_field.send_keys(Keys.BACKSPACE)
            last_name_field.send_keys(last_name)

    def change_employee_id(self, id):
        with allure.step(f"Change employee id to {id}"):
            employee_id_field = self.wait.until(EC.element_to_be_clickable(Fields.EMPLOYEE_ID_FIELD))
            employee_id_field.send_keys(Keys.CONTROL + "a")
            employee_id_field.send_keys(Keys.BACKSPACE)
            employee_id_field.send_keys(id)

    def change_license_id(self, license_id):
        with allure.step(f"Change license id to {license_id}"):
            license_id_field = self.wait.until(EC.element_to_be_clickable(Fields.DRIVER_LICENSE_NUMBER_FIELD))
            license_id_field.send_keys(Keys.CONTROL + "a")
            license_id_field.send_keys(Keys.BACKSPACE)
            license_id_field.send_keys(license_id)

    def change_license_expiry_date_by_input(self, date):
        with allure.step(f"Change license expiry date to {date}"):
            expiry_field = self.wait.until(EC.element_to_be_clickable(Fields.DRIVER_LICENSE_EXPIRY_DATE_FIELD))
            expiry_field.send_keys(Keys.CONTROL + "a")
            expiry_field.send_keys(Keys.BACKSPACE)
            expiry_field.send_keys(date)

    def change_nationality(self, nationality):
        with allure.step(f"Change nationality to {nationality}"):
            nationality_field = self.wait.until(EC.element_to_be_clickable(Fields.NATIONALITY_FIELD))
            nationality_field.click()
            self.wait.until(EC.element_to_be_clickable(('xpath', '//span[text() = "' + nationality + '"]'))).click()

    def change_marital_status(self, status):
        with allure.step(f"Change marital status to {status}"):
            marital_status_field = self.wait.until(EC.element_to_be_clickable(Fields.MARITAL_STATUS_FIELD))
            marital_status_field.click()
            self.wait.until(EC.element_to_be_clickable(('xpath', '//span[text() = "' + status + '"]'))).click()

    def change_date_of_birth_by_input(self, date):
        with allure.step(f"Change date of birth to {date}"):
            date_of_birth_field = self.wait.until(EC.element_to_be_clickable(Fields.DATE_OF_BIRTH_FIELD))
            date_of_birth_field.send_keys(Keys.CONTROL + "a")
            date_of_birth_field.send_keys(Keys.BACKSPACE)
            date_of_birth_field.send_keys(date)

    def change_gender(self, gender):
        with allure.step(f"Change gender to {gender}"):
            self.wait.until(EC.element_to_be_clickable(('xpath', '//label[text() = "' + gender + '"]'))).click()

    @allure.step("Click on 'Save' button for personal info")
    def save_personal_changes(self):
        self.wait.until(EC.element_to_be_clickable(Fields.PERSONAL_SAVE_BUTTON)).click()

    @allure.step("Get error message")
    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(Fields.ERROR_MESSAGE)).text
    
    @allure.step("Check that settings applied successfully")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(Fields.SPINNER))
