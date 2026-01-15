import glob
import os
import time

import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


"""
Что действительно нужно для скачивания PDF:
plugins.always_open_pdf_externally: True - главный параметр

download.default_directory - путь для сохранения

driver.execute_cdp_cmd("Page.setDownloadBehavior") - обязательная настройка через CDP

--disable-pdf-viewer (опционально, но рекомендуется) - отключает встроенный просмотрщик
"""


# Путь для скачивания
path_download = "/Users/andrey/PycharmProjects/PythonProject/Files_downloads/"

# Настройки Chrome
chrome_options = Options()

# Самые важные настройки для скачивания PDF
chrome_options.add_argument("--disable-pdf-viewer")

# Ключевые настройки через prefs
prefs = {
    "download.default_directory": path_download,
    "plugins.always_open_pdf_externally": True,  # Самый важный параметр для PDF
}

chrome_options.add_experimental_option("prefs", prefs)

# Запускаем браузер
driver = webdriver.Chrome(options=chrome_options)

# Настройка через CDP (обязательно для скачивания)
driver.execute_cdp_cmd(
    "Page.setDownloadBehavior",
    {
        "behavior": "allow",
        "downloadPath": path_download,
    }
)

# Переходим на страницу
driver.get('https://www.lambdatest.com/selenium-playground/download-file-demo')
driver.maximize_window()
time.sleep(1)

# Скачиваем файл
button_download = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
button_download.click()
time.sleep(2)
print("Кнопка Download File нажата")

time.sleep(2)

# Директория не пустая
if os.listdir(path_download):
    print("File is here")
else:
    print("File isn't here")

# Создаем директорию

# print(os.listdir(path_downloads))

# Наличие требуемого файла в директории
file_name = 'LambdaTest.pdf'

file_path = path_download + file_name
assert os.access(file_path, os.F_OK) == True
print("File is in directory")

# Файл не пуст
files = glob.glob(os.path.join(path_download, "*.*"))

for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print("File isn't empty")
    else:
        print("File is empty")

# Удаление после проверки
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    os.remove(file)
print("File was deleted")
