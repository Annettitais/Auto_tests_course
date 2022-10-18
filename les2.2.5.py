import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value')
    print(x_element)
    x = x_element.text
    y = calc(x)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    element1 = browser.find_element(By.CSS_SELECTOR, '.form-group .form-control').send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[ID='robotCheckbox']").click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(30)
    browser.quit()
