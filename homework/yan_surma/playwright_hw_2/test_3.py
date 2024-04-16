import time

from playwright.sync_api import Page, expect


def test_click_if_button_is_red(page: Page):
    time.sleep(3)
    page.goto('https://demoqa.com/dynamic-properties')
    red_button = page.locator('//button[@id="colorChange"]')
    expect(red_button).to_have_css('color', 'rgb(220, 53, 69)')
    red_button.click()
    time.sleep(3)
