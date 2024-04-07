import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


def test_check_that_text_appears(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_btn = driver.find_element(By.XPATH, '//button')
    start_btn.click()
    time.sleep(2)
    hello_text_locator = ('xpath', '//div[@id="finish"]/h4')
    hello = wait(driver, 15).until(EC.presence_of_element_located(hello_text_locator))
    hello_text = hello.text
    assert hello_text == 'Hello World!'
