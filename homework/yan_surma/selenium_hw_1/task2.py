import time
from homework.yan_surma.selenium_hw_1.form_page import FormPage


def test_fill_registration_form(driver):
    form = FormPage(driver)
    form.open()
    form.scroll_page()
    form.first_name().send_keys('Yan')
    form.last_name().send_keys('Surma')
    form.email_input().send_keys('testmail@mail.com')
    form.radio_button().click()
    form.number().send_keys('7777777777')
    form.pick_date('22 Jan 2000')
    form.select_subject('Computer Science')
    form.checkbox1().click()
    form.checkbox3().click()
    form.textarea().send_keys('USA, California, Fresno, 3932 Heritage Road')
    form.select_city('NCR')
    form.select_state('Delhi')
    form.scroll_to_bottom()
    form.submit_button().click()
    time.sleep(3)
    form.print_form_info()
    time.sleep(3)
    form.close_button().click()
