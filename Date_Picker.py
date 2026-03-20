import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url_demoqa = "https://demoqa.com/date-picker"
driver.get(url_demoqa)
driver.maximize_window()

"""Сайт https://demoqa.com/date-picker"""

'''1 Заполнение даты через ввод даты'''

# new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# # new_date.clear() - не дал очистить поле. Делаем костыль:
# new_date.send_keys(Keys.BACKSPACE*10)
# time.sleep(1)
# new_date.send_keys("02/02/2024")
# time.sleep(1)
# new_date.send_keys(Keys.RETURN)
# time.sleep(1)
# print("New date - OK")

'''2 Заполнение даты через Date Picker модалку - любая дата'''

# new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# new_date.click()
# time.sleep(1)
# date_12_23_2025 = driver.find_element(By.XPATH, "//div[@aria-label='Choose Tuesday, December 23rd, 2025']")
# date_12_23_2025.click()
# time.sleep(1)
# print("date_12_23_2025 - OK")

'''3 Заполнение даты через Date Picker модалку - TODAY'''

new_date_today = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date_today.click()
time.sleep(1)
today_date = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]")

'''
часть, по которой будем искать атрибут: 'react-datepicker__day--today' (можно и "today" оставить просто)
полезно, когда class составной из многих частей через __ или пробелы, как ниже:
class = 'react-datepicker__day react-datepicker__day--011 react-datepicker__day--selected react-datepicker__day--today'
'''

today_date.click()
time.sleep(3)
print("today_date - OK")

utc_now = datetime.datetime.utcnow()
moscow_time = utc_now + datetime.timedelta(hours=3)
current_date = int(moscow_time.strftime("%d"))  # "Y%-%m-%d_%H-%M-%S"
print(f"Today is {current_date}")
# Today is 11

current_date_new = int(current_date) + 1 # 12
locator = "//div[@aria-label='Choose Friday, December " + str(current_date_new) + "th, 2025']"
print(locator)
# //div[@aria-label='Choose Friday, December 12th, 2025']

new_date_today_new = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date_today_new.click()
time.sleep(2)
today_date_new = driver.find_element(By.XPATH, locator)
today_date_new.click()
time.sleep(2)
print(f"'Date + 1 day is' {current_date_new}")
# 'Date + 1 day is' 12


'''
Я, чтобы не мучиться с 'th' или 'st' в локаторе взял за основу другой XPATH:

driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--023']")
 

Как видите на конце есть число 023.

Далее всё делаем как показал Alex:

#Текущая дата
now_date = datetime.datetime.utcnow().strftime("%d")
print(now_date)

# Переведём текущую дату в числовой тип данных и прибавим один день чтобы получить завтрашнюю дату
int_date = int(now_date) + 1
print(int_date)
 

А вот дальше я эту дату форматирую в зависимости от разрядности числа:

# Форматируем дату в нужный формат локатора
if len(str(int_date)) == 1:
    int_date = "00" + str(int_date)
else:
    int_date = "0" + str(int_date)
То есть если у нас дата от 1 до 9 я преобразую число в строку и прибаляю "00" 

Если дата двузначная от 10 до 31, то при0.
3бавляю "0"

И далее использую обучную конструкцию для локатора:

locator = "//div[@class='react-datepicker__day react-datepicker__day--" + str(int_date) + "']"
'''