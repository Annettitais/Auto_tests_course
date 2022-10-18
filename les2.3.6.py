import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(elements2):
    return str(math.log(abs(12 * math.sin(int(elements2)))))
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    elements1 = browser.find_element(By.CSS_SELECTOR, '[class="trollface btn btn-primary"]').click()
    browser.switch_to.window(browser.window_handles[1])
    elements2 = browser.find_element(By.CSS_SELECTOR, '[ID="input_value"]').text
    elements3 = browser.find_element(By.CSS_SELECTOR, '[ID="answer"]').send_keys(calc(elements2))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(15)
    browser.quit()
