import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException  # импортируем нужное исключение

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'  # для Chrome - начало работы со страницей до полной загрузки всех элементов
# options.add_experimental_option("detach", True)  # Чтобы автоматически не закрывался браузер
# g = Service()  # Управляет процессом ChromeDriver (остановка / запуск), передача доп. парам. в него

driver = webdriver.Chrome(options=options) # Внутри можно передать (options=options, service=g)

# driver.get("https://demoqa.com/dynamic-properties")  # для теста 1
driver.get("https://demoqa.com/radio-button")  # для теста 2
driver.maximize_window()
time.sleep(3)

# тест 1

# time.sleep(6)  # Плохая практика, т.к. время будет суммироваться по ходу всех тестов
# try:
#     visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
#     visible_button.click()
# except NoSuchElementException as exception:
#     print("NoSuchElementException exception")
#     time.sleep(10)
#     visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
#     visible_button.click()
#     print("Click visible_button")

"""Можно использовать сценарий, если надо перезагрузить страницу driver.refresh() или добавить ожидание, чтобы 
обработать ошибку"""

# тест 2

yes_radiobutton = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_radiobutton.click()
try:
    message = driver.find_element(By.XPATH,"//p[@class=(contains(text(), 'selected'))]")
    value_message = message.text
    print(value_message)
    assert value_message == "You have selected No"
except AssertionError as exception:  # указываем ожидаемое исключение
    driver.refresh()
    yes_radiobutton = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_radiobutton.click()
    message = driver.find_element(By.XPATH,"//p[@class=(contains(text(), 'selected'))]")  # //span[@class='text-success']
    value_message = message.text
    print(value_message)
    assert value_message == "You have selected Yes"
print("Test over")