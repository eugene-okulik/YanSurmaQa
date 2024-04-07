import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_select_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    dropdown = Select(driver.find_element(By.XPATH, '//select[@id="id_choose_language"]'))
    dropdown.select_by_visible_text('C#')
    time.sleep(2)
    dropdown_text = dropdown.first_selected_option.text
    submit_btn = driver.find_element(By.XPATH, '//input[@id="submit-id-submit"]')
    submit_btn.click()
    time.sleep(2)
    result_text = driver.find_element(By.XPATH, '//p[@id="result-text"]').text
    assert dropdown_text == result_text, 'Entered text not equal to result text'
    time.sleep(2)
