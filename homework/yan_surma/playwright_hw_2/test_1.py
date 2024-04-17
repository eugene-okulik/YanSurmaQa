import time

from playwright.sync_api import Page, Dialog, expect


def test_accept_and_fill_alert(page: Page):
    def accept_alert(alert: Dialog):
        alert.accept()

    time.sleep(3)
    page.on('dialog', accept_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    click_button = page.locator('//a[@class="a-button"]')
    click_button.click()
    result_text = page.locator('//p[@class="result-text"]')
    expect(result_text).to_contain_text('Ok')
    time.sleep(3)
