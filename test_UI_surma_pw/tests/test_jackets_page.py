import allure

from conftest import jackets


@allure.feature('Smoke')
def test_add_item_sort_by_position(jackets):
    jackets.open_page(jackets.page_url)
    jackets.sort_by_option('Position')
    jackets.hover_on_item_banner()
    item_price = jackets.get_item_price()
    jackets.click_add_to_card_button()
    jackets.check_item_price(item_price)


@allure.feature('Smoke')
def test_add_item_sort_by_price(jackets):
    jackets.open_page(jackets.page_url)
    jackets.sort_by_option('price')
    jackets.hover_on_item_banner()
    item_price = jackets.get_item_price()
    jackets.click_add_to_card_button()
    jackets.check_item_price(item_price)


@allure.feature('Smoke')
def test_add_item_sort_by_product_name(jackets):
    jackets.open_page(jackets.page_url)
    jackets.sort_by_option('Product Name')
    jackets.hover_on_item_banner()
    item_price = jackets.get_item_price()
    jackets.click_add_to_card_button()
    jackets.check_item_price(item_price)
