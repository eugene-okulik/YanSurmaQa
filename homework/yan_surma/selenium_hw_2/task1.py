from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_added_item_equal_in_cart(driver):
    driver.implicitly_wait(5)
    driver.get('https://www.demoblaze.com/index.html')
    item = driver.find_element(By.XPATH, '//a[contains(text(), "Samsung galaxy s6")]')
    item_name = item.text
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(item)
    actions.key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_button = driver.find_element(By.XPATH, '//a[contains(text(), "Add to cart")]')
    add_button.click()
    sleep(2)
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.XPATH, '//a[@id="cartur"]')
    cart.click()
    item_value = driver.find_element(By.XPATH, '//td[contains(text(), "Samsung galaxy s6")]')
    assert item_value.text == item_name
