import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Установка пути к драйверу браузера (Chrome)
driver = webdriver.Chrome()

# Открытие сайта ya.ru
driver.get("https://ya.ru")

element = driver.find_element(By.XPATH, "//input[@class='search3__input mini-suggest__input']")
element.send_keys("Hello world")

button = driver.find_element(By.XPATH, "//button[contains(text(),'Найти')]")
button.click()

s = driver.current_url
print(s)


# Ждем некоторое время для загрузки результатов поиска
time.sleep(5)

# Закрытие браузера
driver.quit()
