import allure
from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.locators import login_page_locators as loc


class LoginPage(BasePage):
    page_url = '/customer/account/login'

    @allure.step('Fill email field')
    def fill_email(self, email_value):
        email_field = self.find(loc.EMAIL_FIELD)
        email_field.fill(email_value)

    @allure.step('Fill password field')
    def fill_password(self, passw_value):
        email_field = self.find(loc.PASSWORD_FIELD)
        email_field.fill(passw_value)

    @allure.step('Click sign in button')
    def click_sign_in_button(self):
        sign_in_button = self.find(loc.SIGN_IN_BUTTON)
        sign_in_button.click()

    @allure.step('Check for email error message')
    def check_for_email_error(self):
        email_error = self.find(loc.EMAIL_ERROR)
        expect(email_error).to_be_visible()
        expect(email_error).to_have_text('This is a required field.')

    @allure.step('Check for password error message')
    def check_for_password_error(self):
        password_error = self.find(loc.PASSWORD_ERROR)
        expect(password_error).to_be_visible()
        expect(password_error).to_have_text('This is a required field.')

    @allure.step('Check for login error message')
    def check_for_login_error(self):
        login_error = self.find(loc.LOGIN_ERROR)
        expect(login_error).to_be_visible()
        expect(login_error).to_have_text(
            'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
        )
