from playwright.sync_api import BrowserContext
import pytest

from pages.account_page import MyAccount
from pages.create_account_page import CreateAccountPage
from pages.eco_page import EcoFriendlyPage
from pages.login_page import LoginPage


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def create_acc(page):
    return CreateAccountPage(page)


@pytest.fixture()
def acc(page):
    return MyAccount(page)


@pytest.fixture()
def login(page):
    return LoginPage(page)


@pytest.fixture()
def eco(page):
    return EcoFriendlyPage(page)
