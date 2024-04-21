from time import sleep

import allure

from pages.base_page import BasePage
from pages.locators import jackets_page_locators as loc


class JacketsPage(BasePage):
    page_url = '/women/tops-women/jackets-women.html'

    @allure.step('Hover on item banner')
    def hover_on_item_banner(self):
        item_banner = self.find(loc.ITEM_BANNER)
        item_banner.hover()

    @allure.step('Click add to card button')
    def click_add_to_card_button(self):
        add_to_card_button = self.find(loc.ADD_TO_CARD_BUTTON)
        add_to_card_button.click()

    @allure.step('Get item price')
    def get_item_price(self):
        item_name = self.find(loc.ITEM_PRICE)
        return item_name.inner_text()

    @allure.step('Check item price')
    def check_item_price(self, item_price_value):
        sleep(2)
        page_item_price = self.find(loc.PAGE_ITEM_PRICE).inner_text()
        assert page_item_price == item_price_value, f'Price {page_item_price} not equal to {item_price_value}'

    @allure.step('Switch to list view')
    def switch_to_list_view(self):
        list_view = self.find(loc.LIST_VIEW)
        list_view.click()

    @allure.step('Sort by option')
    def sort_by_option(self, option):
        sorter = self.find(loc.SORTER)
        sorter.select_option(option)
