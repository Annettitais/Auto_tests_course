import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser=webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    element1=browser.find_element(By.NAME, 'firstname').send_keys('Test')
    element2=browser.find_element(By.NAME, 'lastname').send_keys('Test')
    element3=browser.find_element(By.NAME, 'email').send_keys('email@mail.ru')
    element4=browser.find_element(By.NAME, 'file').send_keys('C:\\avtotext.txt')
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(15)
    browser.quit()
