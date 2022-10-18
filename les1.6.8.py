from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    ##Ввод имени
    elements1 = browser.find_element(By.NAME, "first_name")
    elements1.send_keys('Иван')
    ##Ввод фамилии
    elements2 = browser.find_element(By.NAME, "last_name")
    elements2.send_keys('Петров')
    ##Ввод города
    elements3 = browser.find_element(By.CLASS_NAME, "city")
    elements3.send_keys('Санкт-Петербург')
    ##Ввод города
    elements4 = browser.find_element(By.ID, "country")
    elements4.send_keys('Россия')
    button = browser.find_element(By.XPATH, '/html/body/div/form/div[6]/button[3]')
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(30)
    browser.quit()

