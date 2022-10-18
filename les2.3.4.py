import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(elements2):
    return str(math.log(abs(12 * math.sin(int(elements2)))))


try:
    ##Присваиваем ссылку
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    ##Нажимаем на кнопку
    elements = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()
    confirm = browser.switch_to.alert.accept()
    elements2 = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    rez = calc(elements2)
    elements3 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(rez)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(15)
    browser.quit()
