import allure
from playwright.sync_api import Page, Locator, expect

from pages.locators import base_page_locators as loc


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open page')
    def open_page(self, url):
        return self.page.goto(self.base_url + self.page_url)

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    @allure.step('Check that page title equals')
    def check_page_title(self, title_value):
        page_title = self.find(loc.PAGE_TITLE)
        expect(page_title).to_be_visible()
        expect(page_title).to_have_text(title_value)
