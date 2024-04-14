from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    auth_link = page.get_by_role('link', name='Form Authentication')
    auth_link.click()
    page_title = page.get_by_role('heading', name='Login Page')
    expect(page_title).to_contain_text('Login Page')
    username_field = page.get_by_role('textbox', name='username')
    password_field = page.get_by_role('textbox', name='password')
    username_field.fill('tomsmith')
    password_field.fill('SuperSecretPassword!')
    login_button = page.get_by_role('button')
    login_button.click()
