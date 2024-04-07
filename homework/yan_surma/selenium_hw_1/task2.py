import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_fill_registration_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    scroll = driver.find_element(By.XPATH, '//h5')
    driver.execute_script("arguments[0].scrollIntoView();", scroll)

    first_name_input = driver.find_element(By.XPATH, '//input[@id="firstName"]')
    first_name_input.send_keys('Yan')

    last_name_input = driver.find_element(By.XPATH, '//input[@id="lastName"]')
    last_name_input.send_keys('Surma')

    email_input = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    email_input.send_keys('testmail@gmail.com')

    radio_btn = driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
    radio_btn.click()

    number_input = driver.find_element(By.XPATH, '//input[@id="userNumber"]')
    number_input.send_keys('7777777777')

    datepicker = driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]')
    datepicker.click()
    datepicker.send_keys(Keys.CONTROL + 'a')
    datepicker.send_keys('22 Jan 2000')
    datepicker.send_keys(Keys.ENTER)

    dropdown = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    dropdown.send_keys('Computer Science')
    dropdown.send_keys(Keys.ENTER)

    checkbox1 = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    checkbox1.click()

    checkbox3 = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]')
    checkbox3.click()

    textarea = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
    textarea.send_keys('USA, California, Fresno, 3932 Heritage Road')

    select_city = driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
    select_city.send_keys('NCR')
    select_city.send_keys(Keys.ENTER)

    select_state = driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
    select_state.send_keys('Delhi')
    select_state.send_keys(Keys.ENTER)

    submit_btn = driver.find_element(By.XPATH, '//button[@id="submit"]')
    submit_btn.click()
    time.sleep(5)

    labels = driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
    values = driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
    for label, value in zip(labels, values):
        print(f'{label.text}: {value.text}')
    time.sleep(5)

    close_btn = driver.find_element(By.XPATH, '//button[@id="closeLargeModal"]')
    close_btn.click()
