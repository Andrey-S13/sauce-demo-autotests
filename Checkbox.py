import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

"""Сайт https://demoqa.com/radio-button"""

driver = webdriver.Chrome()
url_checkbox = "https://demoqa.com/checkbox"
driver.get(url_checkbox)
driver.maximize_window()


# Находим видимую часть
checkbox_home = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
checkbox_home.click()
# checkbox_home.click()
time.sleep(1)
print("checkbox_home clicked")

# Указываем к видимой части скрытый "input", чтобы чекбокс прошел проверку на True:
tree_node_elem = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(f"checkbox_home_checked - {tree_node_elem[0].is_selected()}") # Вернет True - проверка, что чекбокс активирован

# checkbox_home_checked = driver.find_element(By.CLASS_NAME, "rct-icon-check")
# assert checkbox_home_checked.is_displayed()  # Проверка, что чекбокс активирован
# print("checkbox_home_checked - OK")

'''
Есть подозрение, что is_selected не может обработать обращение непосредственно к чек-боксу 
(т.к на верстке сайта сам чек-бокс находится в теге span)

Поэтому для того чтобы проверить активен ли чек-бокс в этом случае необходимо учитывать 2 момента:
1) Мы находим два элемента — скрытый input и видимую часть чекбокса, представленную элементом span.
Кликаем на видимую часть (span).
2) Используем метод is_selected() на найденном элементе input, чтобы убедиться, что чекбокс установлен.
'''


# button_dropdown_home = driver.find_element(By.XPATH, "//button[@class='rct-collapse rct-collapse-btn']")
# button_dropdown_home.click()
# time.sleep(1)
# print("dropdown_home clicked")
#
# name = driver.find_element(By.XPATH, "(//span[@class='rct-title'])[2]")
# value_name = name.text
# assert value_name == 'Desktop'
# print(f"Check field {value_name} - OK")
#
# checkbox_desktop = driver.find_element(By.XPATH, "(//span[@class='rct-title'])[2]")
# checkbox_desktop.click()
# time.sleep(1)
# print("checkbox_desktop clicked")
#
# button_dropdown_desktop = driver.find_element(By.XPATH, "(//button[@class='rct-collapse rct-collapse-btn'])[2]")
# button_dropdown_desktop.click()
# time.sleep(1)
# print("dropdown_desktop clicked")
#
# checkbox_notes_unchecked = driver.find_element(By.CLASS_NAME, "rct-icon-uncheck")
# assert checkbox_notes_unchecked.is_displayed()  # Проверка, что чекбокс деактивирован
# print("checkbox_notes_unchecked - OK")
#
# name_two = driver.find_element(By.XPATH, "(//span[@class='rct-title'])[3]")
# value_name_two = name_two.text
# assert value_name_two == 'Notes'
# print(f"Check field {value_name_two} - OK")


"""Сайт https://testpages.herokuapp.com/pages/forms/html-form/"""

driver = webdriver.Chrome()
url = "https://testpages.herokuapp.com/styled/basic-html-form-test.html"
driver.get(url)
driver.maximize_window()

checkbox_1 = driver.find_element(By.XPATH, "//input[@value='cb1']")
checkbox_1_location = checkbox_1.location  # Узнаем координаты элемента X, Y
driver.execute_script(f"window.scrollTo(0, {checkbox_1_location['y']})")  # пролистываем на Y пикселей вниз
time.sleep(1)  # пауза, чтобы произошло пролистывание
checkbox_1.click()
time.sleep(1)
print("checkbox_1 clicked")