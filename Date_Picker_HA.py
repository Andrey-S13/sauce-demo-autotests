import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url_demoqa = "https://demoqa.com/date-picker"
driver.get(url_demoqa)
driver.maximize_window()

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# очистка текущей даты
new_date.send_keys(Keys.BACKSPACE*10)
# нахождение текущей даты + прибавление 10 дней
utc_now = datetime.datetime.utcnow()
msk_now = utc_now + datetime.timedelta(hours=3, days=10)
# установка нужного формата текущей даты
msk_now_our_format = msk_now.strftime("%m/%d/%y") # "Y%-%m-%d_%H-%M-%S" - можно любой сет задавать
print("Новая дата: ", msk_now_our_format)
# запись нового значения в поле
new_date.send_keys(msk_now_our_format)
time.sleep(2)
new_date.send_keys(Keys.ENTER)
time.sleep(2)
print("Select Date - OK")
