from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    value = browser.find_element(By.ID, "treasure")
    x_element = value.get_attribute("valuex")
    x = x_element
    y = calc(x)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

