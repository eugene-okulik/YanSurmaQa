import allure
from playwright.sync_api import expect

from generator.generator import generated_user
from pages.locators import create_account_page_locators as loc
from pages.base_page import BasePage


class CreateAccountPage(BasePage):
    page_url = 'customer/account/create/'

    @allure.step('Fill first name field')
    def fill_first_name(self, value):
        first_name_field = self.find(loc.FIRST_NAME_FIELD)
        first_name_field.fill(value)

    @allure.step('Fill last name field')
    def fill_last_name(self, value):
        last_name_field = self.find(loc.LAST_NAME_FIELD)
        last_name_field.fill(value)

    @allure.step('Fill email field')
    def fill_email(self, value):
        email_field = self.find(loc.EMAIL_FIELD)
        email_field.fill(value)

    @allure.step('Fill password field')
    def fill_password(self, value):
        password_field = self.find(loc.PASSWORD_FIELD)
        password_field.fill(value)

    @allure.step('Fill password confirmation field')
    def fill_password_confirmation(self, value):
        confirm_password_field = self.find(loc.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.fill(value)

    @allure.step('Click create button')
    def click_create_button(self):
        create_button = self.find(loc.CREATE_BUTTON)
        create_button.click()

    @allure.step('Check for success auth alert')
    def check_for_success_auth_alert(self):
        success_alert = self.find(loc.SUCCESS_AUTH_ALERT)
        expect(success_alert).to_be_visible()
        success_message = 'Thank you for registering with Main Website Store.'
        expect(success_alert).to_have_text(success_message)

    @allure.step('Check for field error messages')
    def check_for_field_error_messages(self):
        error_message = 'This is a required field.'
        error_alerts = self.page.get_by_text(error_message)
        expect(error_alerts).to_have_text(error_message)

    @allure.step('Check for password error message')
    def check_for_password_error_messages(self):
        error_message = 'Please enter the same value again.'
        error_alerts = self.page.get_by_text(error_message)
        expect(error_alerts).to_have_text(error_message)

    @allure.step('Fill authorization form')
    # Methods
    def fill_authorization_form(self):
        user = next(generated_user())
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_password(user.password)
        self.fill_password_confirmation(user.confirm_password)
        self.click_create_button()
        return [user.first_name, user.last_name, user.email]
