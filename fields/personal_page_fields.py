

class PersonalPageFields:

    FIRST_NAME_FIELD = ('xpath', '//input[@name="firstName"]')
    MIDDLE_NAME_FIELD = ('xpath', '//input[@name="middleName"]')
    LAST_NAME_FIELD = ('xpath', '//input[@name="lastName"]')
    PERSONAL_SAVE_BUTTON = ('xpath', '(//button[@type="submit"])[1]')
    CUSTOM_SAVE_BUTTON = ('xpath', '(//button[@type="submit"])[2]')
    SPINNER = ('xpath', '//div[@class="oxd-loading-spinner"]')
    EMPLOYEE_ID_FIELD = ('xpath', "(//input[@class='oxd-input oxd-input--active'])[2]")
    ERROR_MESSAGE = ('xpath', '//div[contains(@class, "oxd-input-field-error-message)]')
    DRIVER_LICENSE_NUMBER_FIELD = ('xpath', "(//input[@class='oxd-input oxd-input--active'])[4]")
    DRIVER_LICENSE_EXPIRY_DATE_FIELD = ('xpath', "(//input[@class='oxd-input oxd-input--active'])[5]")
    MARITAL_STATUS_FIELD = ('xpath', '(//div[@class="oxd-select-text-input"])[2]')
    NATIONALITY_FIELD = ('xpath', '(//div[@class="oxd-select-text-input"])[1]')
    DATE_OF_BIRTH_FIELD = ('xpath', '(//input[@class="oxd-input oxd-input--active"])[6]')