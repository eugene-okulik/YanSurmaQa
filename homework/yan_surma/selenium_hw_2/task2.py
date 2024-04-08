from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_added_item_equal_in_cart(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    driver.execute_script("window.scrollBy(0, 500)")
    backpack = driver.find_element(By.XPATH, '(//a[contains(text(), "Push It Messenger Bag")])[1]')
    backpack_name = backpack.text
    actions = ActionChains(driver)
    add_to_compare = driver.find_element(By.XPATH, '(//a[@title="Add to Compare"])[1]')
    actions.move_to_element(backpack).click(add_to_compare).perform()
    driver.execute_script("window.scrollBy(0, 500)")
    sleep(3)
    compare = driver.find_element(By.XPATH, '(//a[contains(text(), "Push It Messenger Bag")])[2]')
    assert compare.text == backpack_name, 'Item name not equal to compare name'
