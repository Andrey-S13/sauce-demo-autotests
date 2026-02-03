import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome()
driver.get("https://www.testmu.ai/selenium-playground/upload-file-demo/")
driver.maximize_window()
time.sleep(1)

path_upload = "/Users/andrey/PycharmProjects/PythonProject/Files_upload/Снимок экрана 2026-01-11 в 22.24.14.png"

click_button = driver.find_element(By.XPATH, "//input[@class='w-full']")
click_button.send_keys(path_upload)
time.sleep(3)

successful_text = "File Successfully Uploaded"

text_successful_upload = driver.find_element(By.XPATH, "//div[@id='error']")
value_text_successful_upload = text_successful_upload.text
assert value_text_successful_upload == successful_text
time.sleep(2)
print("assert 1 - OK")

# Полное наименование файла на компе

computer_file_name = "Снимок экрана 2026-01-11 в 22.24.14.png"

# Находим, какой путь сохраняет браузер в value
# value - это атрибут, который содержит у <input type="file"> полный путь к файлу / имя файла

value_upload_path = click_button.get_attribute("value")
print(value_upload_path)
# C:\fakepath\Снимок экрана 2026-01-11 в 22.24.14.png - полученное значение
# fakepath - скрывает полный путь для безопасности (в современных браузерах везде)


# Шлифуем название файла

import re

value_upload_path = "C:\fakepath\Снимок экрана 2026-01-11 в 22.24.14.png"  # полученный путь в браузере

match = re.search(r'[\\/]([^\\/]+)$', value_upload_path)

# Без r пришлось бы писать: '[\\\\/]([^\\\\/]+)$'
# Фактически, перечисляем символы, которые нам нужны: \ и /
# Символ \ нужно экранировать как \\
# Ищет ЛЮБОЙ из этих символов: \ или /
# [^  ] - отрицание (не ищем другие элементы, кроме перечисленных)
# + - одно и более совпадений
# $ - якорь. Нужен, чтобы текст брался до конца строки

if match:
    browser_file_name = match.group(1)
    print(browser_file_name)
    # Снимок экрана 2026-01-11 в 22.24.14.png

# Сверяем название подгруженного файла / факт подгрузки файла (НЕ на сервер)

current_file_name = driver.find_element(By.CSS_SELECTOR, "input#file.w-full")
value_current_file_name = current_file_name.text
print(value_current_file_name)
assert computer_file_name == browser_file_name
time.sleep(2)
print("assert 2 - OK")

