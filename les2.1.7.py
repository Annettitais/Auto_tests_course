from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element(By.ID, 'treasure')
    x_element = x_element.get_attribute('valuex')
    x = int(x_element)
    y = calc(x)
    element1 = browser.find_element(By.CSS_SELECTOR, "[ID='answer']")
    element1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[ID='robotCheckbox']").click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(30)
    browser.quit()
