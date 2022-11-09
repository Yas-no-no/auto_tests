from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #int(x) + int(y)
    def sum(x, y):
        return str(x + y)

    value1 = browser.find_element(By.ID, "num1")
    value2 = browser.find_element(By.ID, "num2")
    x = int(value1.text)
    y = int(value2.text)
    z = sum(x, y)

    browser.find_element(By.CSS_SELECTOR, "[value='" + z + "']").click()

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



