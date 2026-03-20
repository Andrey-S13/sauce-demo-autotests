import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url_demoqa = "https://demoqa.com/buttons"
driver.get(url_demoqa)
driver.maximize_window()

"""Сайт https://demoqa.com/buttons"""
'''
1) Открыли сайт и создали переменную "action"
которая является экземпляром класса "ActionChains()", в котором мы передаем "driver" - переменную, 
которая хранит экземпляр нашего драйвера для хром "webdriver.Chrome()"

2) создали переменную "double_click_button" с локатором нашей кнопки 

3) Обращаемся к нашему экземпляру класса "ActionChains()", т.е. к переменной "action", в которой вызываем 
метод "double_click". Далее вызываем метод "perform()" для сохранения нашего действия
'''
action = ActionChains(driver)
double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_click_button).perform()
time.sleep(1)

double_click_button_text = driver.find_element(By.CSS_SELECTOR, "p#doubleClickMessage")
full_text = double_click_button_text.text
assert "You have done a double click" in full_text
print("double_click - OK")

action = ActionChains(driver)
right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click).perform()
time.sleep(1)

right_click_text = driver.find_element(By.CSS_SELECTOR, "p#rightClickMessage")
full_text_two = right_click_text.text
assert "You have done a right click" in full_text_two
print("right_click - OK")
