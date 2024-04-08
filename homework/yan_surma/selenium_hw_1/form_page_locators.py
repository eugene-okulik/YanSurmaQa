from selenium.webdriver.common.by import By

class FormPageLocators:
    FIRST_NAME_LOCATOR = By.XPATH, '//input[@id="firstName"]'
    LAST_NAME_LOCATOR = By.XPATH, '//input[@id="lastName"]'
    EMAIL_LOCATOR = By.XPATH, '//input[@id="userEmail"]'
    RADIO_BUTTON_LOCATOR = By.XPATH, '//label[@for="gender-radio-1"]'
    NUMBER_LOCATOR = By.XPATH, '//input[@id="userNumber"]'
    DATE_PICKER_LOCATOR = By.XPATH, '//input[@id="dateOfBirthInput"]'
    SUBJECTS_DROPDOWN_LOCATOR = By.XPATH, '//input[@id="subjectsInput"]'
    CHECKBOX_1_LOCATOR = By.XPATH, '//label[@for="hobbies-checkbox-1"]'
    CHECKBOX_3_LOCATOR = By.XPATH, '//label[@for="hobbies-checkbox-3"]'
    TEXTAREA_LOCATOR = By.XPATH, '//textarea[@id="currentAddress"]'
    CITY_SELECTOR_LOCATOR = By.XPATH, '//input[@id="react-select-3-input"]'
    STATE_SELECTOR_LOCATOR = By.XPATH, '//input[@id="react-select-4-input"]'
    SUBMIT_BUTTON_LOCATOR = By.XPATH, '//button[@id="submit"]'
    LABELS_LOCATORS = By.XPATH, '//tbody/tr/td[1]'
    VALUES_LOCATORS = By.XPATH, '//tbody/tr/td[2]'
    CLOSE_BUTTON_LOCATOR = By.XPATH, '//button[@id="closeLargeModal"]'
