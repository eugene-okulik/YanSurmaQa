import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_input_text_equals_to_response_text(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    field = driver.find_element(By.XPATH, '//input[@id="id_text_string"]')
    field.send_keys('first_test_input')
    time.sleep(2)
    field_text = field.get_attribute("value")
    field.send_keys(Keys.ENTER)
    time.sleep(2)
    result_text = driver.find_element(By.XPATH, '//p[@id="result-text"]').text
    assert field_text == result_text, 'Entered text not equal to result text'
    time.sleep(2)
