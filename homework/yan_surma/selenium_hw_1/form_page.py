import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Locators
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


class FormPage:

    def __init__(self, driver):
        self.driver = driver

    # Elements
    def open(self):
        self.driver.get('https://demoqa.com/automation-practice-form')

    def scroll_page(self):
        scroll = self.driver.find_element(By.XPATH, '//h5')
        return self.driver.execute_script("arguments[0].scrollIntoView();", scroll)

    def first_name(self):
        return self.driver.find_element(*FIRST_NAME_LOCATOR)

    def last_name(self):
        return self.driver.find_element(*LAST_NAME_LOCATOR)

    def email_input(self):
        return self.driver.find_element(*EMAIL_LOCATOR)

    def radio_button(self):
        return self.driver.find_element(*RADIO_BUTTON_LOCATOR)

    def number(self):
        return self.driver.find_element(*NUMBER_LOCATOR)

    def date_picker(self):
        return self.driver.find_element(*DATE_PICKER_LOCATOR)

    def subjects_dropdown(self):
        return self.driver.find_element(*SUBJECTS_DROPDOWN_LOCATOR)

    def checkbox1(self):
        return self.driver.find_element(*CHECKBOX_1_LOCATOR)

    def checkbox3(self):
        return self.driver.find_element(*CHECKBOX_3_LOCATOR)

    def textarea(self):
        return self.driver.find_element(*TEXTAREA_LOCATOR)

    def city_selector(self):
        return self.driver.find_element(*CITY_SELECTOR_LOCATOR)

    def state_selector(self):
        return self.driver.find_element(*STATE_SELECTOR_LOCATOR)

    def submit_button(self):
        return self.driver.find_element(*SUBMIT_BUTTON_LOCATOR)

    def labels(self):
        return self.driver.find_elements(*LABELS_LOCATORS)

    def values(self):
        return self.driver.find_elements(*VALUES_LOCATORS)

    def close_button(self):
        return self.driver.find_element(*CLOSE_BUTTON_LOCATOR)

    # Actions
    def pick_date(self, date):
        self.date_picker().click()
        self.date_picker().send_keys(Keys.CONTROL + 'a')
        self.date_picker().send_keys(date)
        self.date_picker().send_keys(Keys.ENTER)

    def select_subject(self, subject):
        self.subjects_dropdown().send_keys(subject)
        self.subjects_dropdown().send_keys(Keys.ENTER)

    def select_city(self, city):
        self.city_selector().send_keys(city)
        self.city_selector().send_keys(Keys.ENTER)

    def select_state(self, state):
        self.state_selector().send_keys(state)
        self.state_selector().send_keys(Keys.ENTER)

    def print_form_info(self):
        for label, value in zip(self.labels(), self.values()):
            print(f'{label.text}: {value.text}')
        time.sleep(5)

    def scroll_to_bottom(self):  # Скролл в самый низ страницы
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
