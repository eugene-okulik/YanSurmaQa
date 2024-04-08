import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from homework.yan_surma.selenium_hw_1.form_page_locators import FormPageLocators


class FormPage(FormPageLocators):

    def __init__(self, driver):
        self.driver = driver

    # Elements
    def open(self):
        self.driver.get('https://demoqa.com/automation-practice-form')

    def scroll_page(self):
        scroll = self.driver.find_element(By.XPATH, '//h5')
        return self.driver.execute_script("arguments[0].scrollIntoView();", scroll)

    def first_name(self):
        return self.driver.find_element(*self.FIRST_NAME_LOCATOR)

    def last_name(self):
        return self.driver.find_element(*self.LAST_NAME_LOCATOR)

    def email_input(self):
        return self.driver.find_element(*self.EMAIL_LOCATOR)

    def radio_button(self):
        return self.driver.find_element(*self.RADIO_BUTTON_LOCATOR)

    def number(self):
        return self.driver.find_element(*self.NUMBER_LOCATOR)

    def date_picker(self):
        return self.driver.find_element(*self.DATE_PICKER_LOCATOR)

    def subjects_dropdown(self):
        return self.driver.find_element(*self.SUBJECTS_DROPDOWN_LOCATOR)

    def checkbox1(self):
        return self.driver.find_element(*self.CHECKBOX_1_LOCATOR)

    def checkbox3(self):
        return self.driver.find_element(*self.CHECKBOX_3_LOCATOR)

    def textarea(self):
        return self.driver.find_element(*self.TEXTAREA_LOCATOR)

    def city_selector(self):
        return self.driver.find_element(*self.CITY_SELECTOR_LOCATOR)

    def state_selector(self):
        return self.driver.find_element(*self.STATE_SELECTOR_LOCATOR)

    def submit_button(self):
        return self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)

    def labels(self):
        return self.driver.find_elements(*self.LABELS_LOCATORS)

    def values(self):
        return self.driver.find_elements(*self.VALUES_LOCATORS)

    def close_button(self):
        return self.driver.find_element(*self.CLOSE_BUTTON_LOCATOR)

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
