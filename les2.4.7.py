from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
browser.find_element(By.CSS_SELECTOR, '[ID="book"]').click()

##Пролистываем
button2 = browser.find_element(By.ID, "solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
x = browser.find_element(By.CSS_SELECTOR, '[ID="input_value"]').text
rez=calc(x)
button3 = browser.find_element(By.CSS_SELECTOR, '[ID="answer"]').send_keys(rez)
browser.find_element(By.CSS_SELECTOR, '#solve').click()
