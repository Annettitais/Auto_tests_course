from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    ##Значение x
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    element1 = browser.find_element(By.CSS_SELECTOR, '.form-group .form-control')
    element1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(30)
    browser.quit()
