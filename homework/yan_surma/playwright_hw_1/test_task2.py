import time

from playwright.sync_api import Page
import locators as loc


def test_fill_form(page: Page):
    # Fill form
    page.goto('https://demoqa.com/automation-practice-form')
    first_name_field = page.locator(loc.FIRST_NAME)
    first_name_field.fill('Test first name')
    last_name_field = page.locator(loc.LAST_NAME)
    last_name_field.fill('Test last name')
    email_field = page.locator(loc.EMAIL)
    email_field.fill('test@test.com')
    radio_button = page.locator(loc.RADIO_BUTTON)
    radio_button.click()
    number_field = page.locator(loc.MOBILE_NUMBER)
    number_field.fill('1234567890')
    date_picker = page.locator(loc.DATE_PICKER)
    date_picker.click()
    date_picker.fill('22 Jan 2000')
    date_picker.press('Enter')
    subjets_dropdown = page.locator(loc.SUBJECTS_DROPDOWN)
    subjets_dropdown.fill('Computer science')
    subjets_dropdown.press('Enter')
    checkbox_1 = page.locator(loc.CHECKBOX_1)
    checkbox_1.click()
    checkbox_3 = page.locator(loc.CHECKBOX_3)
    checkbox_3.click()
    current_address_field = page.locator(loc.CURRENT_ADDRESS)
    current_address_field.fill('Texas, Austin, 1321 Ashton Lane')
    state_dropdown = page.locator(loc.STATE_DROPDOWN)
    state_dropdown.click()
    state_option = page.locator(loc.STATE_OPTION)
    state_option.click()
    city_dropdown = page.locator(loc.CITY_DROPDOWN)
    city_dropdown.click()
    city_option = page.locator(loc.CITY_OPTION)
    city_option.click()
    submit_button = page.locator(loc.SUBMIT_BUTTON)
    submit_button.click()
    time.sleep(10)
    # Print form info
    labels = page.locator(loc.LABELS).all_text_contents()
    values = page.locator(loc.VALUES).all_text_contents()
    for label, value in zip(labels, values):
        print(f'{label}:{value}')
