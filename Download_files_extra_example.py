
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

path_download = "/Users/andrey/PycharmProjects/PythonProject/Files_downloads"

# Создаем папку, если не существует
if not os.path.exists(path_download):
    os.makedirs(path_download)

# Настройки Chrome
chrome_options = Options()

# Ключевые аргументы
chrome_options.add_argument("--disable-features=DownloadBubble")  # Отключаем новое меню загрузок
chrome_options.add_argument("--disable-pdf-viewer")  # Отключаем встроенный PDF просмотрщик
chrome_options.add_argument("--disable-features=PDFViewerUpdate")  # Отключаем обновления PDF viewer
chrome_options.add_argument("--disable-features=UseOzonePlatform")  # Для стабильности

# Настройки для скачивания PDF
prefs = {
    "download.default_directory": path_download,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,  # Ключевая настройка для PDF
    "profile.default_content_settings.popups": 0,
    "profile.default_content_setting_values.automatic_downloads": 1,

    # Явно указываем MIME-типы для скачивания
    "browser.helperApps.neverAsk.saveToDisk": "application/pdf,application/octet-stream",
    "browser.download.manager.showWhenStarting": False,
    "browser.download.folderList": 2,
}

chrome_options.add_experimental_option("prefs", prefs)

# Запускаем браузер
driver = webdriver.Chrome(options=chrome_options)

# Устанавливаем поведение через CDP (самый надежный способ)
driver.execute_cdp_cmd(
    "Browser.setDownloadBehavior",
    {
        "behavior": "allow",
        "downloadPath": path_download,
        "eventsEnabled": True
    }
)

# Дополнительные настройки через CDP
driver.execute_cdp_cmd("Emulation.setUserAgentOverride", {
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
})

driver.get('https://www.lambdatest.com/selenium-playground/download-file-demo')
time.sleep(2)

# Кликаем для скачивания
button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
button.click()
time.sleep(5)

print("Загрузка начата...")