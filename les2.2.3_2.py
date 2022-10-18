from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
try:
    browser=webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    ##Ищем сумму
    sum1=int(browser.find_element(By.CSS_SELECTOR, '#num1').text)+int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
    ##Выбираем значение из списка
    spisok=Select(browser.find_element(By.TAG_NAME, 'select'))
    spisok.select_by_value(str(sum1))
    ##Отправляем результатэ
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(30)
    browser.quit()

