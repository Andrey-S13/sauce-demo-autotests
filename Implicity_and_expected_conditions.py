import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException  # импортируем нужное исключение
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
https://www.geeksforgeeks.org/python/exceptions-selenium-python/
какие бывают типы ошибок

WebDriverWait - это класс для ожидания определенного условия в течение заданного времени.
Используется для явного ожидания появления или выполнения определенного условия перед продолжением
выполнения кода.
Работает с ожидаемыми условиями, которые определяют, какое условие должно быть выполнено, чтобы продолжить
выполнение кода.

Если за 30сек, к примеру, не сможем нажать на элемент, появится ошибка TimeoutException

Есть различные условия ожидания:

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable — it is Displayed and Enabled.
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
'''

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'  # для Chrome - начало работы со страницей до полной загрузки всех элементов
# options.add_experimental_option("detach", True)  # Чтобы автоматически не закрывался браузер
# g = Service()  # Управляет процессом ChromeDriver (остановка / запуск), передача доп. парам. в него

driver = webdriver.Chrome(options=options) # Внутри можно передать (options=options, service=g)

driver.get("https://demoqa.com/dynamic-properties")  # для теста 1
# driver.get("https://demoqa.com/radio-button")  # для теста 2
driver.maximize_window()
driver.implicitly_wait(10)  # неявное ожидание. Время ожидания, пока наш элемент не появитяс в DOM
# применяется ко всем элементам в тесте (не надо указывать, как time.sleep(), каждый раз)
# т.е. наш элемент может отработать на 2, 5, 10 сек, но на 11 уже упадет ошибка "элемент не найден"
# NoSuchElementException
time.sleep(3)



"""Неявное ожидание (Implicit Wait) - это установка времени, в течении которого элемент появится в DOM 
(схема страницы, которая написана на HTML - гипертекстовая разметка языка)"""

# driver.implicitly_wait(10) - все элементы будут ждать до 10 сек

# print("start test")
# visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
# visible_button.click()
# print("finish test")

"""Явное ожидание (Explicit Wait) - это индивидуальное ожидание для каждого элемента. 
Можем устанавливать ожидания от какого-либо действия.
К примеру visible - элемент видно в DOM и на странице
или clickable - на элемент можно нажать"""

# visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']")))
# ждем, пока кнопка станет кликабельной 30 сек, ждем, когда элемент
# появится на странице, ждем, пока текст в элементе изменится и т.д.


"""Вместе использовать явное и неявное ожидание НЕЛЬЗЯ"""

print("start test")
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']")))
# по-умолчанию частота взаимодействия с элементом 0,5с
visible_button.click()
print("finish test")