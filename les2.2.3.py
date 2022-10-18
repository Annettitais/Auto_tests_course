import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    x = (browser.find_element(By.CSS_SELECTOR, "#num1")).text
    y = (browser.find_element(By.CSS_SELECTOR, "#num2")).text
    z=int(x)+int(y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(30)
    browser.quit()
