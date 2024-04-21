import allure

from pages.base_page import BasePage
from pages.locators import account_page_locators as loc


class MyAccount(BasePage):
    page_url = '/customer/account/'

    @allure.step('Check for account info equals')
    def check_for_account_info_equals(self, first_name, last_name, email):
        account_text = self.find(loc.ACCOUNT_INFO).inner_text()
        split_text = account_text.split(sep='\n')
        name_value, email_value = split_text[0], split_text[1]
        account_name = first_name + ' ' + last_name
        assert account_name == name_value, f"Expected {account_name}, but got {name_value}"
        assert email == email_value, f"Expected {email}, but got {email_value}"
